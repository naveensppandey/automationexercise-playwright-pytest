class BasePage:
    """
    BasePage is the parent class for all Page Objects in this framework.
    It contains simple, reusable actions like navigate, click, fill, and get_text.
    """

    def __init__(self, page):
        # Store Playwright page object
        self.page = page

    def navigate(self, url):
        # Open URL in browser tab
        self.page.goto(url, wait_until="domcontentloaded")

    def click(self, selector):
        # Click element using Playwright locator
        self.page.locator(selector).click()

    def fill(self, selector, text):
        # Fill input field using Playwright locator
        self.page.locator(selector).fill(text)

    def get_text(self, selector):
        # Get text content from element
        return self.page.locator(selector).inner_text().strip()

    def is_visible(self, selector, timeout=5000):
        # Check if element becomes visible on page within timeout
        try:
            self.page.locator(selector).first.wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False



