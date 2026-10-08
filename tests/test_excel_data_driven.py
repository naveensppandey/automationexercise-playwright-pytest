import pytest
from utils.excel_data_provider import read_excel_data

# Read 50 test cases from test_cases.xlsx
excel_cases = read_excel_data("test_data/test_cases.xlsx")

@pytest.mark.parametrize("tc", excel_cases)
def test_excel_data_driven_cases(tc):
    """
    Data-Driven Test: Validates test case metadata read from Excel sheet.
    Runs once for each of the 50 test cases in test_cases.xlsx.
    """
    # Verify that essential fields exist in each row
    assert "Test Case ID" in tc and tc["Test Case ID"].startswith("TC")
    assert "Module" in tc and len(tc["Module"]) > 0
    assert "Test Case" in tc and len(tc["Test Case"]) > 0
    assert "Expected Result" in tc and len(tc["Expected Result"]) > 0

    print(f"\n[Excel Data-Driven] Executed {tc['Test Case ID']} ({tc['Module']}): {tc['Test Case']}")
