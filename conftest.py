import pytest
from playwright.sync_api import sync_playwright

def pytest_configure(config):
    """Register custom marker so pytest recognizes @pytest.mark.tc_id."""
    config.addinivalue_line("markers", "tc_id(*ids): associate test with Excel test case ID")

def pytest_addoption(parser):
    """Command-line options to customize browser execution."""
    parser.addoption("--headed", action="store_true", default=False, help="Run browser in headed mode")
    parser.addoption("--browser", action="store", default="chromium", help="Browser type: chromium or firefox")

@pytest.fixture
def page(request):
    """
    Pytest Fixture for Playwright browser setup and teardown.
    - Launches browser before each test.
    - Aborts external ad networks to keep test execution fast and reliable.
    - Passes 'page' to each test function.
    - Closes context and browser cleanly after the test completes.
    """
    is_headed = request.config.getoption("--headed")
    browser_name = request.config.getoption("--browser").lower()

    with sync_playwright() as playwright:
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

        # Abort third-party ad requests that can stall automationexercise.com navigation
        context.route("**/*google-analytics*", lambda route: route.abort())
        context.route("**/*googlesyndication*", lambda route: route.abort())
        context.route("**/*doubleclick*", lambda route: route.abort())
        context.route("**/*adservice*", lambda route: route.abort())
        context.route("**/*pagead*", lambda route: route.abort())
        context.route("**/*adsbygoogle*", lambda route: route.abort())

        page_instance = context.new_page()

        yield page_instance

        context.close()
        browser.close()
