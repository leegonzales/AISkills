#!/usr/bin/env python3
"""Extract and analyze formulas from an Excel file for auditing."""

import sys
import json
import re
from pathlib import Path
from collections import defaultdict
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, column_index_from_string

# Excel error values to detect
EXCEL_ERRORS = {'#REF!', '#DIV/0!', '#VALUE!', '#N/A', '#NAME?', '#NULL!', '#NUM!', '#GETTING_DATA'}

# Volatile functions that recalculate on every change
VOLATILE_FUNCTIONS = {'NOW', 'TODAY', 'RAND', 'RANDBETWEEN', 'INDIRECT', 'OFFSET', 'INFO', 'CELL'}

# Common function categories
FUNCTION_CATEGORIES = {
    'lookup': {'VLOOKUP', 'HLOOKUP', 'INDEX', 'MATCH', 'XLOOKUP', 'LOOKUP', 'CHOOSE'},
    'financial': {'NPV', 'IRR', 'XIRR', 'XNPV', 'PMT', 'FV', 'PV', 'RATE', 'NPER', 'SLN', 'DB', 'DDB'},
    'statistical': {'AVERAGE', 'STDEV', 'VAR', 'MEDIAN', 'MODE', 'CORREL', 'FORECAST', 'TREND', 'GROWTH'},
    'logical': {'IF', 'IFS', 'AND', 'OR', 'NOT', 'SWITCH', 'IFERROR', 'IFNA'},
    'aggregation': {'SUM', 'SUMIF', 'SUMIFS', 'COUNT', 'COUNTIF', 'COUNTIFS', 'SUMPRODUCT', 'AGGREGATE'},
    'text': {'CONCATENATE', 'CONCAT', 'LEFT', 'RIGHT', 'MID', 'LEN', 'TRIM', 'SUBSTITUTE', 'TEXT'},
    'date': {'DATE', 'YEAR', 'MONTH', 'DAY', 'EOMONTH', 'EDATE', 'NETWORKDAYS', 'WORKDAY'},
}

def parse_cell_reference(ref: str) -> tuple:
    """Parse a cell reference like 'A1' or '$A$1' into (col, row)."""
    ref = ref.replace('$', '')
    match = re.match(r'^([A-Za-z]+)(\d+)$', ref)
    if match:
        return (match.group(1).upper(), int(match.group(2)))
    return None

def extract_references_from_formula(formula: str) -> list:
    """Extract cell and range references from a formula."""
    refs = []
    # Match cell references like A1, $A$1, Sheet1!A1, 'Sheet Name'!A1
    pattern = r"(?:'[^']+'!|[A-Za-z_]+!)?(?:\$?[A-Za-z]+\$?\d+(?::\$?[A-Za-z]+\$?\d+)?)"
    matches = re.findall(pattern, formula)
    return matches

def extract_functions_from_formula(formula: str) -> list:
    """Extract function names from a formula."""
    pattern = r'([A-Z][A-Z0-9_.]+)\s*\('
    return re.findall(pattern, formula.upper())

def calculate_nesting_depth(formula: str) -> int:
    """Calculate maximum nesting depth of a formula."""
    max_depth = 0
    current_depth = 0
    for char in formula:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1
    return max_depth

def extract_formulas(filepath: str, max_cells: int = 50000) -> dict:
    """Extract and analyze all formulas from Excel file."""
    result = {
        "filename": Path(filepath).name,
        "formulas": [],
        "errors_found": [],
        "volatile_functions": [],
        "function_usage": defaultdict(int),
        "complexity_metrics": {},
        "issues": [],
        "formula_patterns": defaultdict(list),  # Track similar formulas
    }

    try:
        wb = load_workbook(filepath, read_only=False, data_only=False)
    except Exception as e:
        result["error"] = f"Failed to load: {str(e)}"
        return result

    cells_processed = 0
    formulas_by_pattern = defaultdict(list)

    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        sheet_formulas = []

        for row in ws.iter_rows():
            if cells_processed >= max_cells:
                result["truncated"] = True
                break

            for cell in row:
                cells_processed += 1

                # Check for formula
                if cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
                    formula = cell.value
                    cell_addr = f"{sheet_name}!{cell.coordinate}"

                    formula_info = {
                        "cell": cell_addr,
                        "formula": formula[:500],  # Truncate very long formulas
                        "length": len(formula),
                        "functions": extract_functions_from_formula(formula),
                        "references": extract_references_from_formula(formula)[:20],
                        "nesting_depth": calculate_nesting_depth(formula),
                    }

                    # Track function usage
                    for func in formula_info["functions"]:
                        result["function_usage"][func] += 1

                    # Check for volatile functions
                    volatile_used = [f for f in formula_info["functions"] if f in VOLATILE_FUNCTIONS]
                    if volatile_used:
                        result["volatile_functions"].append({
                            "cell": cell_addr,
                            "volatile_functions": volatile_used
                        })

                    # Flag complex formulas
                    if formula_info["nesting_depth"] > 3:
                        result["issues"].append({
                            "type": "high_nesting",
                            "severity": "warning",
                            "cell": cell_addr,
                            "detail": f"Nesting depth: {formula_info['nesting_depth']}"
                        })

                    if len(formula) > 200:
                        result["issues"].append({
                            "type": "long_formula",
                            "severity": "info",
                            "cell": cell_addr,
                            "detail": f"Formula length: {len(formula)} chars"
                        })

                    # Create pattern key for grouping similar formulas
                    pattern_key = re.sub(r'\d+', '#', formula)[:100]
                    formulas_by_pattern[pattern_key].append(cell_addr)

                    result["formulas"].append(formula_info)

                # Check for error values in calculated results
                elif cell.value in EXCEL_ERRORS:
                    result["errors_found"].append({
                        "cell": f"{sheet_name}!{cell.coordinate}",
                        "error": str(cell.value),
                        "severity": "critical"
                    })

    # Analyze formula consistency
    for pattern, cells in formulas_by_pattern.items():
        if len(cells) >= 3:  # Pattern appears in 3+ cells
            result["formula_patterns"][pattern[:50]] = {
                "count": len(cells),
                "sample_cells": cells[:5]
            }

    # Calculate complexity metrics
    all_nesting = [f["nesting_depth"] for f in result["formulas"]]
    all_lengths = [f["length"] for f in result["formulas"]]

    result["complexity_metrics"] = {
        "total_formulas": len(result["formulas"]),
        "total_errors": len(result["errors_found"]),
        "volatile_function_count": len(result["volatile_functions"]),
        "avg_nesting_depth": round(sum(all_nesting) / len(all_nesting), 2) if all_nesting else 0,
        "max_nesting_depth": max(all_nesting) if all_nesting else 0,
        "avg_formula_length": round(sum(all_lengths) / len(all_lengths), 1) if all_lengths else 0,
        "max_formula_length": max(all_lengths) if all_lengths else 0,
        "unique_patterns": len(formulas_by_pattern),
    }

    # Categorize function usage
    category_counts = defaultdict(int)
    for func, count in result["function_usage"].items():
        for category, funcs in FUNCTION_CATEGORIES.items():
            if func in funcs:
                category_counts[category] += count
                break
    result["function_categories"] = dict(category_counts)

    # Infer purpose from function usage
    if category_counts.get('financial', 0) > 5:
        result["inferred_purpose"] = "Financial model"
    elif category_counts.get('lookup', 0) > category_counts.get('aggregation', 0):
        result["inferred_purpose"] = "Data lookup/reference system"
    elif category_counts.get('aggregation', 0) > 10:
        result["inferred_purpose"] = "Reporting/aggregation tool"
    elif category_counts.get('date', 0) > 5:
        result["inferred_purpose"] = "Scheduling/timeline tracker"
    else:
        result["inferred_purpose"] = "General purpose spreadsheet"

    # Convert defaultdicts to regular dicts for JSON
    result["function_usage"] = dict(result["function_usage"])
    result["formula_patterns"] = dict(result["formula_patterns"])

    wb.close()
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_formulas.py <excel_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    result = extract_formulas(filepath)
    print(json.dumps(result, indent=2, default=str))
