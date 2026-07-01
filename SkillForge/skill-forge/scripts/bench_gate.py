#!/usr/bin/env python3
"""SkillForge promotion gate over a benchmark.json.

Turns the standard Agent Skills `benchmark.json` (produced by the vendored
`aggregate_benchmark.py`) into a non-gameable PROMOTE / HOLD / REVERT verdict,
operationalizing SkillForge's stop discipline:

  - Lift is measured *within-run* as with_skill − without_skill on pass_rate.
  - A lift smaller than the noise band is INCONCLUSIVE, not a win ("you measured nothing").
  - Must-pass expectations that regress force a REVERT regardless of average lift.
  - An optional prior benchmark guards against regression vs the current best.

The upstream tooling stops at aggregation + a viewer; this is the gate on top.
Deterministic and offline — no model calls — so it is CI-safe and testable with fixtures.

Usage:
    python bench_gate.py <candidate benchmark.json> \
        [--baseline <prior benchmark.json>] \
        [--evals <evals.json>] \
        [--min-margin 0.10] [--min-win-rate 0.6] \
        [--history <history.json>] [--json]

Exit code: 0 on PROMOTE, 1 on HOLD/REVERT (usable as a CI gate).
"""

import argparse
import json
import sys
from pathlib import Path

# --- Defaults (justified, not voodoo) ---------------------------------------
# Minimum lift we require *on top of* the measured noise band before calling a
# win. 0.10 = a 10-percentage-point pass-rate gain; below this, skill value is
# not worth a promotion even if nominally positive.
DEFAULT_MIN_MARGIN = 0.10
# Fraction of evals where with_skill must strictly beat without_skill. A skill
# that helps on average but loses on 40% of tasks is not yet reliable.
DEFAULT_MIN_WIN_RATE = 0.60
# Floor on the noise band when stddev is ~0 (e.g. single run). LLM-judge scores
# swing ~0.5-1.0 on a 0-4 scale (~0.12-0.25 normalized); 0.10 is a conservative
# floor so a zero-variance fluke can't manufacture a clean win.
NOISE_FLOOR = 0.10

WITH = "with_skill"
WITHOUT = "without_skill"


def _mean(summary: dict, config: str, metric: str) -> float:
    return summary.get(config, {}).get(metric, {}).get("mean", 0.0)


def _stddev(summary: dict, config: str, metric: str) -> float:
    return summary.get(config, {}).get(metric, {}).get("stddev", 0.0)


def win_rate(runs: list[dict]) -> tuple[float, int, int]:
    """Fraction of evals where with_skill mean pass_rate strictly beats without_skill."""
    by_eval: dict[int, dict[str, list[float]]] = {}
    for r in runs:
        cfg = r.get("configuration")
        if cfg not in (WITH, WITHOUT):
            continue
        pr = r.get("result", {}).get("pass_rate", 0.0)
        by_eval.setdefault(r.get("eval_id"), {}).setdefault(cfg, []).append(pr)
    wins = comparable = 0
    for _eval_id, cfgs in by_eval.items():
        if WITH not in cfgs or WITHOUT not in cfgs:
            continue
        comparable += 1
        w = sum(cfgs[WITH]) / len(cfgs[WITH])
        b = sum(cfgs[WITHOUT]) / len(cfgs[WITHOUT])
        if w > b:
            wins += 1
    rate = wins / comparable if comparable else 0.0
    return rate, wins, comparable


def must_pass_regressions(runs: list[dict], must_pass: list[str]) -> list[dict]:
    """Return must-pass violations: a with_skill run where a matching expectation failed.

    Matching is substring (case-insensitive) of a must-pass statement against the
    expectation text. Must-pass statements that match no expectation are reported
    separately (they need manual/red-team confirmation — the gate can't check them).
    """
    violations = []
    matched_statements: set[str] = set()
    for r in runs:
        if r.get("configuration") != WITH:
            continue
        for exp in r.get("expectations", []):
            text = (exp.get("text") or "").lower()
            for mp in must_pass:
                if mp.lower() in text or text in mp.lower():
                    matched_statements.add(mp)
                    if not exp.get("passed", False):
                        violations.append({
                            "must_pass": mp,
                            "eval_id": r.get("eval_id"),
                            "run_number": r.get("run_number"),
                            "evidence": exp.get("evidence", ""),
                        })
    unmatched = [mp for mp in must_pass if mp not in matched_statements]
    return violations, unmatched


def evaluate(candidate: dict, baseline: dict | None, must_pass: list[str],
             min_margin: float, min_win_rate: float) -> dict:
    summary = candidate.get("run_summary", {})
    runs = candidate.get("runs", [])

    with_mean = _mean(summary, WITH, "pass_rate")
    without_mean = _mean(summary, WITHOUT, "pass_rate")
    lift = with_mean - without_mean
    noise_band = max(_stddev(summary, WITH, "pass_rate"),
                     _stddev(summary, WITHOUT, "pass_rate"),
                     NOISE_FLOOR)
    required = max(noise_band, min_margin)
    wr, wins, comparable = win_rate(runs)
    violations, unmatched = must_pass_regressions(runs, must_pass)

    # Regression vs prior best (guards a promotion that quietly drops vs last best).
    regression = None
    if baseline is not None:
        base_with = _mean(baseline.get("run_summary", {}), WITH, "pass_rate")
        drop = base_with - with_mean
        if drop > noise_band:
            regression = {"prior_with_skill": base_with, "candidate_with_skill": with_mean,
                          "drop": round(drop, 4)}

    # --- Verdict -----------------------------------------------------------
    reasons = []
    if violations:
        verdict = "REVERT"
        reasons.append(f"{len(violations)} must-pass regression(s) in with_skill runs")
    elif regression is not None:
        verdict = "REVERT"
        reasons.append(f"regressed vs prior best by {regression['drop']:.2f} (> noise {noise_band:.2f})")
    elif lift < required and lift <= noise_band:
        verdict = "HOLD"
        reasons.append(f"lift {lift:+.2f} is within the noise band (±{noise_band:.2f}) — inconclusive; add tasks/judges")
    elif lift >= required and wr >= min_win_rate:
        verdict = "PROMOTE"
        reasons.append(f"lift {lift:+.2f} clears required {required:.2f} and win-rate {wr:.0%} >= {min_win_rate:.0%}")
    else:
        verdict = "HOLD"
        if lift < required:
            reasons.append(f"lift {lift:+.2f} below required margin {required:.2f}")
        if wr < min_win_rate:
            reasons.append(f"win-rate {wr:.0%} below required {min_win_rate:.0%} ({wins}/{comparable} evals)")

    return {
        "verdict": verdict,
        "reasons": reasons,
        "metrics": {
            "with_skill_pass_rate": round(with_mean, 4),
            "without_skill_pass_rate": round(without_mean, 4),
            "lift": round(lift, 4),
            "noise_band": round(noise_band, 4),
            "required_margin": round(required, 4),
            "win_rate": round(wr, 4),
            "wins": wins,
            "comparable_evals": comparable,
        },
        "must_pass_violations": violations,
        "must_pass_unchecked": unmatched,
        "regression_vs_prior": regression,
    }


def load_json(path: str) -> dict:
    return json.loads(Path(path).read_text())


def main() -> int:
    p = argparse.ArgumentParser(description="SkillForge promotion gate over benchmark.json")
    p.add_argument("candidate", help="Path to candidate benchmark.json")
    p.add_argument("--baseline", help="Path to prior/best benchmark.json (regression guard)")
    p.add_argument("--evals", help="Path to evals.json (reads top-level _must_pass)")
    p.add_argument("--must-pass", action="append", default=[],
                   help="A must-pass statement (repeatable); merged with evals.json _must_pass")
    p.add_argument("--min-margin", type=float, default=DEFAULT_MIN_MARGIN)
    p.add_argument("--min-win-rate", type=float, default=DEFAULT_MIN_WIN_RATE)
    p.add_argument("--history", help="Append the verdict to this history.json")
    p.add_argument("--json", action="store_true", help="Emit verdict as JSON only")
    args = p.parse_args()

    candidate = load_json(args.candidate)
    baseline = load_json(args.baseline) if args.baseline else None
    must_pass = list(args.must_pass)
    if args.evals:
        must_pass += load_json(args.evals).get("_must_pass", [])

    result = evaluate(candidate, baseline, must_pass, args.min_margin, args.min_win_rate)

    if args.history:
        hist_path = Path(args.history)
        history = json.loads(hist_path.read_text()) if hist_path.exists() else {"verdicts": []}
        history.setdefault("verdicts", []).append({
            "skill_name": candidate.get("metadata", {}).get("skill_name", ""),
            "timestamp": candidate.get("metadata", {}).get("timestamp", ""),
            "verdict": result["verdict"],
            "lift": result["metrics"]["lift"],
        })
        hist_path.write_text(json.dumps(history, indent=2))

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        m = result["metrics"]
        print(f"VERDICT: {result['verdict']}")
        for r in result["reasons"]:
            print(f"  - {r}")
        print(f"  lift {m['lift']:+.2f}  (with {m['with_skill_pass_rate']:.2f} vs "
              f"without {m['without_skill_pass_rate']:.2f});  noise ±{m['noise_band']:.2f};  "
              f"win-rate {m['win_rate']:.0%} ({m['wins']}/{m['comparable_evals']})")
        if result["must_pass_unchecked"]:
            print(f"  ! {len(result['must_pass_unchecked'])} must-pass statement(s) not "
                  f"machine-checkable — confirm by red-team: {result['must_pass_unchecked']}")

    return 0 if result["verdict"] == "PROMOTE" else 1


if __name__ == "__main__":
    sys.exit(main())
