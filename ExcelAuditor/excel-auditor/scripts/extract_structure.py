#!/usr/bin/env python3
"""Extract structural metadata from an Excel file for auditing."""

import sys
import json
from pathlib import Path
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
import zipfile
import xml.etree.ElementTree as ET

def extract_structure(filepath: str) -> dict:
    """Extract comprehensive structure from Excel file."""
    result = {
        "filename": Path(filepath).name,
        "sheets": [],
        "named_ranges": [],
        "tables": [],
        "external_links": [],
        "has_vba": False,
        "has_hidden_sheets": False,
        "file_size_mb": round(Path(filepath).stat().st_size / (1024 * 1024), 2),
        "summary": {}
    }

    # Check for VBA (macros) by inspecting the zip
    try:
        with zipfile.ZipFile(filepath, 'r') as z:
            result["has_vba"] = any('vbaProject' in name for name in z.namelist())
    except:
        pass

    # Load workbook
    try:
        wb = load_workbook(filepath, read_only=False, data_only=False)
    except Exception as e:
        result["error"] = f"Failed to load: {str(e)}"
        return result

    # Extract sheet info
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        sheet_info = {
            "name": sheet_name,
            "visibility": "visible" if ws.sheet_state == "visible" else ws.sheet_state,
            "dimensions": ws.dimensions or "empty",
            "row_count": ws.max_row or 0,
            "col_count": ws.max_column or 0,
            "has_filters": ws.auto_filter.ref is not None if ws.auto_filter else False,
            "freeze_panes": str(ws.freeze_panes) if ws.freeze_panes else None,
            "merged_cells_count": len(ws.merged_cells.ranges),
        }

        # Sample headers (first row)
        headers = []
        if ws.max_row and ws.max_row > 0:
            for col in range(1, min(ws.max_column + 1, 26)):  # First 25 cols
                cell = ws.cell(row=1, column=col)
                if cell.value:
                    headers.append(str(cell.value)[:50])
        sheet_info["headers_sample"] = headers

        result["sheets"].append(sheet_info)

        if sheet_info["visibility"] != "visible":
            result["has_hidden_sheets"] = True

    # Extract named ranges
    for name in wb.defined_names:
        try:
            defn = wb.defined_names[name]
            result["named_ranges"].append({
                "name": name,
                "refers_to": str(defn.attr_text)[:100] if hasattr(defn, 'attr_text') else str(defn.value)[:100] if hasattr(defn, 'value') else None,
                "scope": "global"
            })
        except:
            pass

    # Extract tables
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        for table in ws.tables.values():
            result["tables"].append({
                "name": table.name,
                "sheet": sheet_name,
                "range": table.ref,
                "display_name": table.displayName
            })

    # Check for external links in formulas (basic check)
    external_patterns = set()
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        for row in ws.iter_rows(max_row=min(ws.max_row or 0, 500)):
            for cell in row:
                if cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
                    formula = cell.value
                    if '[' in formula and ']' in formula:
                        # Extract external reference
                        start = formula.find('[')
                        end = formula.find(']')
                        if start < end:
                            ext_ref = formula[start+1:end]
                            external_patterns.add(ext_ref)

    result["external_links"] = list(external_patterns)[:20]  # Cap at 20

    # Summary stats
    result["summary"] = {
        "total_sheets": len(result["sheets"]),
        "visible_sheets": sum(1 for s in result["sheets"] if s["visibility"] == "visible"),
        "hidden_sheets": sum(1 for s in result["sheets"] if s["visibility"] != "visible"),
        "total_named_ranges": len(result["named_ranges"]),
        "total_tables": len(result["tables"]),
        "external_link_count": len(result["external_links"]),
        "has_vba": result["has_vba"],
        "risk_flags": []
    }

    # Add risk flags
    if result["has_vba"]:
        result["summary"]["risk_flags"].append("Contains VBA macros")
    if result["has_hidden_sheets"]:
        result["summary"]["risk_flags"].append("Has hidden sheets")
    if len(result["external_links"]) > 0:
        result["summary"]["risk_flags"].append(f"External links: {len(result['external_links'])}")
    if any(s["merged_cells_count"] > 50 for s in result["sheets"]):
        result["summary"]["risk_flags"].append("Heavy use of merged cells")

    wb.close()
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_structure.py <excel_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    result = extract_structure(filepath)
    print(json.dumps(result, indent=2, default=str))
