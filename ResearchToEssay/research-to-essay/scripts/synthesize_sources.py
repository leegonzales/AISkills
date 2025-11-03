#!/usr/bin/env python3
"""
Thematic synthesis tool for research-to-essay workflow.
Takes research sources and organizes them by theme with claim extraction.
"""

import json
import sys
from typing import List, Dict, Any
from collections import defaultdict


def extract_claims_from_source(source: Dict[str, Any]) -> List[str]:
    """
    Extract key claims from a source.
    In practice, this would use NLP or be populated by Claude during research.
    For now, it expects claims to be pre-extracted.
    """
    return source.get('claims', [])


def cluster_by_theme(sources: List[Dict[str, Any]]) -> Dict[str, List[Dict]]:
    """
    Group sources and claims by theme.
    
    Expected source format:
    {
        'title': str,
        'url': str,
        'source_type': str,  # 'primary', 'expert', 'commentary', etc.
        'claims': [str],
        'themes': [str],  # tags for thematic grouping
        'date': str,
        'credibility_tier': int  # 1-4
    }
    """
    theme_map = defaultdict(lambda: {
        'sources': [],
        'convergent_claims': [],
        'divergent_claims': []
    })
    
    # First pass: group sources by theme
    for source in sources:
        for theme in source.get('themes', ['uncategorized']):
            theme_map[theme]['sources'].append({
                'title': source['title'],
                'url': source['url'],
                'tier': source.get('credibility_tier', 3),
                'claims': source.get('claims', [])
            })
    
    # Second pass: identify convergent vs divergent claims within themes
    for theme, data in theme_map.items():
        claim_counts = defaultdict(lambda: {'count': 0, 'sources': []})
        
        for source in data['sources']:
            for claim in source['claims']:
                normalized_claim = claim.lower().strip()
                claim_counts[normalized_claim]['count'] += 1
                claim_counts[normalized_claim]['sources'].append(source['title'])
        
        # Convergent: mentioned by multiple sources
        data['convergent_claims'] = [
            {'claim': claim, 'count': info['count'], 'sources': info['sources']}
            for claim, info in claim_counts.items()
            if info['count'] >= 2
        ]
        
        # Divergent: single-source claims (potential tensions)
        data['divergent_claims'] = [
            {'claim': claim, 'source': info['sources'][0]}
            for claim, info in claim_counts.items()
            if info['count'] == 1
        ]
    
    return dict(theme_map)


def generate_synthesis_report(theme_map: Dict[str, Any]) -> str:
    """Generate markdown report of thematic synthesis."""
    
    report = "# Research Synthesis Report\n\n"
    
    for theme, data in sorted(theme_map.items()):
        report += f"## Theme: {theme.title()}\n\n"
        
        # Source overview
        report += f"**Sources ({len(data['sources'])})**:\n"
        for source in data['sources']:
            tier_label = {1: 'Primary', 2: 'Expert', 3: 'Commentary', 4: 'Weak'}
            tier = tier_label.get(source['tier'], 'Unknown')
            report += f"- [{source['title']}]({source['url']}) — *{tier}*\n"
        report += "\n"
        
        # Convergent claims (agreement)
        if data['convergent_claims']:
            report += "**Convergent Claims** (supported by multiple sources):\n"
            for item in sorted(data['convergent_claims'], 
                             key=lambda x: x['count'], 
                             reverse=True):
                report += f"- {item['claim']} "
                report += f"({item['count']} sources: {', '.join(item['sources'][:3])})\n"
            report += "\n"
        
        # Divergent claims (tensions)
        if data['divergent_claims']:
            report += "**Divergent Claims** (single-source, potential tensions):\n"
            for item in data['divergent_claims'][:5]:  # Limit to top 5
                report += f"- {item['claim']} — *{item['source']}*\n"
            report += "\n"
        
        report += "---\n\n"
    
    return report


def main():
    """Main entry point for synthesis script."""
    
    if len(sys.argv) < 2:
        print("Usage: synthesize_sources.py <sources.json>")
        print("\nExpected JSON format:")
        print(json.dumps([{
            'title': 'Source Title',
            'url': 'https://example.com',
            'source_type': 'primary',
            'claims': ['Claim 1', 'Claim 2'],
            'themes': ['theme1', 'theme2'],
            'date': '2025-01-15',
            'credibility_tier': 1
        }], indent=2))
        sys.exit(1)
    
    # Load sources from JSON file
    with open(sys.argv[1], 'r') as f:
        sources = json.load(f)
    
    # Perform thematic clustering
    theme_map = cluster_by_theme(sources)
    
    # Generate synthesis report
    report = generate_synthesis_report(theme_map)
    
    # Output to stdout or file
    if len(sys.argv) > 2:
        with open(sys.argv[2], 'w') as f:
            f.write(report)
        print(f"Synthesis report written to {sys.argv[2]}")
    else:
        print(report)


if __name__ == '__main__':
    main()
