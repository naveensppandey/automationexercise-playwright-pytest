import os
import openpyxl

def read_excel_data(filename="test_data/test_cases.xlsx", sheet_name="TestCases", limit=None):
    """
    Simple function to read an Excel (.xlsx) sheet using openpyxl
    and return rows as a list of dictionaries.
    Optional limit parameter allows loading a subset for automated execution.
    """
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(project_root, filename)

    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook[sheet_name]

    rows = []
    headers = [cell.value for cell in sheet[1]]

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if any(row):
            row_dict = dict(zip(headers, row))
            rows.append(row_dict)
            if limit and len(rows) >= limit:
                break

    workbook.close()
    return rows
