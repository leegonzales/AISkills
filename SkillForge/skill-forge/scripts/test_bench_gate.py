#!/usr/bin/env python3
"""Offline tests for bench_gate.evaluate — no model calls, deterministic.

Run: python3 test_bench_gate.py   (exits 0 on pass, 1 on failure)
"""
import sys

from bench_gate import evaluate


def _summary(w_mean, w_sd, b_mean, b_sd):
    def cfg(m, sd):
        return {"pass_rate": {"mean": m, "stddev": sd},
                "time_seconds": {"mean": 0, "stddev": 0},
                "tokens": {"mean": 0, "stddev": 0}}
    return {"with_skill": cfg(w_mean, w_sd), "without_skill": cfg(b_mean, b_sd)}


def _runs(pairs, expectations_by_eval=None):
    """pairs: list of (eval_id, with_pr, without_pr)."""
    runs = []
    for eid, wpr, bpr in pairs:
        runs.append({"eval_id": eid, "configuration": "with_skill", "run_number": 1,
                     "result": {"pass_rate": wpr},
                     "expectations": (expectations_by_eval or {}).get(eid, [])})
        runs.append({"eval_id": eid, "configuration": "without_skill", "run_number": 1,
                     "result": {"pass_rate": bpr}, "expectations": []})
    return runs


def bench(summary, runs):
    return {"metadata": {"skill_name": "t"}, "run_summary": summary, "runs": runs}


CASES = []


def case(name, got, want):
    ok = got == want
    CASES.append((name, ok, f"got {got}, want {want}"))


# 1. Clear win -> PROMOTE (lift 0.50, low noise, 100% win rate)
r = evaluate(bench(_summary(0.85, 0.05, 0.35, 0.05),
                   _runs([(1, 0.9, 0.3), (2, 0.8, 0.4)])),
             None, [], 0.10, 0.60)
case("clear win promotes", r["verdict"], "PROMOTE")

# 2. Lift inside noise band -> HOLD (lift 0.05, noise 0.20)
r = evaluate(bench(_summary(0.60, 0.20, 0.55, 0.18),
                   _runs([(1, 0.6, 0.55), (2, 0.6, 0.55)])),
             None, [], 0.10, 0.60)
case("noise-band lift holds", r["verdict"], "HOLD")

# 3. Must-pass regression -> REVERT even with big lift
exp = {1: [{"text": "never proposes a runaway loop", "passed": False, "evidence": "did"}]}
r = evaluate(bench(_summary(0.90, 0.03, 0.30, 0.03),
                   _runs([(1, 0.9, 0.3), (2, 0.9, 0.3)], exp)),
             None, ["Never proposes a runaway loop with no ceiling"], 0.10, 0.60)
case("must-pass regression reverts", r["verdict"], "REVERT")

# 4. Regression vs prior best -> REVERT
prior = bench(_summary(0.90, 0.03, 0.30, 0.03), _runs([(1, 0.9, 0.3)]))
cand = bench(_summary(0.60, 0.03, 0.30, 0.03), _runs([(1, 0.6, 0.3), (2, 0.6, 0.3)]))
r = evaluate(cand, prior, [], 0.10, 0.60)
case("regression vs prior reverts", r["verdict"], "REVERT")

# 5. Good lift but low win-rate -> HOLD (helps a lot on 1, loses on 2)
r = evaluate(bench(_summary(0.55, 0.05, 0.40, 0.05),
                   _runs([(1, 0.95, 0.30), (2, 0.35, 0.40), (3, 0.35, 0.40)])),
             None, [], 0.10, 0.60)
case("low win-rate holds", r["verdict"], "HOLD")

# 6. Unmatched must-pass is reported, not silently passed
r = evaluate(bench(_summary(0.85, 0.05, 0.35, 0.05), _runs([(1, 0.9, 0.3), (2, 0.8, 0.4)])),
             None, ["some statement no expectation mentions"], 0.10, 0.60)
case("unmatched must-pass surfaced", bool(r["must_pass_unchecked"]), True)

failed = [c for c in CASES if not c[1]]
for name, ok, detail in CASES:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + ("" if ok else f"  ({detail})"))
print(f"\n{len(CASES) - len(failed)}/{len(CASES)} passed")
sys.exit(1 if failed else 0)
