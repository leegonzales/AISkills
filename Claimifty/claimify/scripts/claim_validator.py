#!/usr/bin/env python3
"""
Validates claim structure for completeness and consistency.
Use when generating JSON format to catch common errors.
"""

import json
import sys

def validate_claims(data):
    """Validate claim structure and relationships."""
    errors = []
    warnings = []
    
    if not isinstance(data, dict):
        errors.append("Data must be a JSON object")
        return errors, warnings
    
    # Check required top-level keys
    if "claims" not in data:
        errors.append("Missing 'claims' array")
        return errors, warnings
    
    claims = data["claims"]
    claim_ids = {c.get("id") for c in claims if "id" in c}
    
    # Validate each claim
    for i, claim in enumerate(claims):
        prefix = f"Claim {i+1}"
        
        # Required fields
        if "id" not in claim:
            errors.append(f"{prefix}: Missing 'id'")
        if "text" not in claim:
            errors.append(f"{prefix}: Missing 'text'")
        if "type" not in claim:
            warnings.append(f"{prefix}: Missing 'type'")
        
        # Valid types
        valid_types = {"factual", "normative", "definitional", "causal", "predictive", "assumption"}
        if "type" in claim and claim["type"] not in valid_types:
            warnings.append(f"{prefix}: Unknown type '{claim['type']}'")
        
        # Check relationship references exist
        for rel_field in ["supports", "opposed_by", "assumes"]:
            if rel_field in claim:
                refs = claim[rel_field]
                if not isinstance(refs, list):
                    errors.append(f"{prefix}: '{rel_field}' must be array")
                else:
                    for ref in refs:
                        if ref not in claim_ids:
                            warnings.append(f"{prefix}: References non-existent claim '{ref}' in '{rel_field}'")
    
    # Check relationships array if present
    if "relationships" in data:
        for i, rel in enumerate(data["relationships"]):
            prefix = f"Relationship {i+1}"
            
            if "from" not in rel:
                errors.append(f"{prefix}: Missing 'from'")
            elif rel["from"] not in claim_ids:
                warnings.append(f"{prefix}: 'from' references non-existent claim")
            
            if "to" not in rel:
                errors.append(f"{prefix}: Missing 'to'")
            elif rel["to"] not in claim_ids:
                warnings.append(f"{prefix}: 'to' references non-existent claim")
    
    return errors, warnings

def main():
    if len(sys.argv) < 2:
        print("Usage: claim_validator.py <claims.json>")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {sys.argv[1]}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}")
        sys.exit(1)
    
    errors, warnings = validate_claims(data)
    
    if errors:
        print("ERRORS:")
        for err in errors:
            print(f"  ❌ {err}")
    
    if warnings:
        print("\nWARNINGS:")
        for warn in warnings:
            print(f"  ⚠️  {warn}")
    
    if not errors and not warnings:
        print("✅ Validation passed")
        sys.exit(0)
    elif errors:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
