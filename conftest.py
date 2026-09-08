import os
import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    # Command line option to run browser in headed mode: pytest --headed
    parser.addoption("--headed", action="store_true", default=False, help="Run browser in headed mode")

@pytest.fixture
def page(request):
    """
    Pytest Fixture for browser setup and teardown.
    - Launches browser before test.
    - Passes 'page' to test.
    - Closes browser after test completes.
    """
    is_headed = request.config.getoption("--headed")
    
    with sync_playwright() as playwright:
        # Launch Chromium browser
        browser = playwright.chromium.launch(headless=not is_headed)
        context = browser.new_context()
        page_instance = context.new_page()
        
        # Give page instance to the test
        yield page_instance
        
        # Close browser after test finishes
        context.close()
        browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest Hook: Automatically captures screenshot on test failure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page_instance = item.funcargs.get("page")
        if page_instance:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}_failure.png"
            page_instance.screenshot(path=screenshot_path)
            print(f"\n[Screenshot Saved] {screenshot_path}")
