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
        # Click on an element
        self.page.locator(selector).click()

    def fill(self, selector, text):
        # Clear field and type text
        self.page.locator(selector).fill(text)

    def get_text(self, selector):
        # Get visible text from an element
        return self.page.locator(selector).inner_text().strip()

    def is_visible(self, selector):
        # Check if element is visible on page
        return self.page.locator(selector).is_visible()
