import os
import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    # Command line options to run browser in headed mode and choose browser (chromium or firefox)
    parser.addoption("--headed", action="store_true", default=False, help="Run browser in headed mode")
    parser.addoption("--browser", action="store", default="chromium", help="Browser type: chromium or firefox")

@pytest.fixture
def page(request):
    """
    Pytest Fixture for browser setup and teardown.
    - Supports Chromium and Firefox browsers via --browser option.
    - Launches browser before test.
    - Passes 'page' to test.
    - Closes browser after test completes.
    """
    is_headed = request.config.getoption("--headed")
    browser_name = request.config.getoption("--browser").lower()
    
    with sync_playwright() as playwright:
        # Launch Chromium or Firefox browser based on option with anti-bot options
        if browser_name == "firefox":
            browser = playwright.firefox.launch(headless=not is_headed)
        else:
            browser = playwright.chromium.launch(
                headless=not is_headed,
                args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
            )

        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 720}
        )
        # Abort third-party ad and analytics requests that stall automationexercise.com navigation
        context.route("**/*google-analytics*", lambda route: route.abort())
        context.route("**/*googlesyndication*", lambda route: route.abort())
        context.route("**/*doubleclick*", lambda route: route.abort())
        context.route("**/*adservice*", lambda route: route.abort())
        context.route("**/*pagead*", lambda route: route.abort())
        context.route("**/*adsbygoogle*", lambda route: route.abort())

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

