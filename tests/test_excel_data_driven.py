import pytest
from utils.excel_data_provider import read_excel_data

# Read a small sample (3 test cases) from test_cases.xlsx repository for automation demo.
# The remaining test cases in test_cases.xlsx serve as documentation for future scope.
excel_sample_cases = read_excel_data("test_data/test_cases.xlsx", limit=3)

@pytest.mark.parametrize("tc", excel_sample_cases)
def test_excel_data_driven_cases(tc):
    """
    Data-Driven Test Example: Demonstrates reading test case data from Excel sheet.
    Executes a sample subset of test cases from the 50-test-case Excel repository.
    """
    assert "Test Case ID" in tc and tc["Test Case ID"].startswith("TC")
    assert "Module" in tc and len(tc["Module"]) > 0
    assert "Test Case" in tc and len(tc["Test Case"]) > 0
    assert "Expected Result" in tc and len(tc["Expected Result"]) > 0

    print(f"\n[Excel Data-Driven Demo] Executed {tc['Test Case ID']} ({tc['Module']}): {tc['Test Case']}")

