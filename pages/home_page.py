from pages.base_page import BasePage

class HomePage(BasePage):
    """HomePage represents the home page (https://automationexercise.com/)."""

    URL = "https://automationexercise.com/"

    # Page Locators
    LOGO = "div.logo img"
    LOGIN_LINK = "a[href='/login']"
    PRODUCTS_LINK = "a[href='/products']"
    CART_LINK = ".shop-menu a[href='/view_cart']"
    CONTACT_US_LINK = "a[href='/contact_us']"
    SUBSCRIBE_EMAIL = "#susbscribe_email"
    SUBSCRIBE_BUTTON = "#subscribe"
    SUBSCRIBE_SUCCESS = "#success-subscribe, .alert-success"
    FOOTER = "#footer"

    def open(self):
        # Open home page
        self.navigate(self.URL)

    def is_loaded(self):
        # Check if home logo is visible
        return self.is_visible(self.LOGO)

    def click_signup_login(self):
        # Click Signup / Login link
        self.click(self.LOGIN_LINK)

    def click_products(self):
        # Click Products link
        self.click(self.PRODUCTS_LINK)

    def click_cart(self):
        # Click Cart link
        self.click(self.CART_LINK)

    def click_contact_us(self):
        # Click Contact Us link
        self.click(self.CONTACT_US_LINK)

    def scroll_to_bottom(self):
        # Scroll to bottom of the page
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.page.wait_for_timeout(500)

    def scroll_to_top(self):
        # Scroll back to the top of the page
        self.page.evaluate("window.scrollTo(0, 0)")
        self.page.wait_for_timeout(500)

    def is_footer_visible(self):
        # Verify footer element is visible
        return self.is_visible(self.FOOTER)

    def subscribe(self, email):
        # Enter email in footer and click subscribe button
        self.fill(self.SUBSCRIBE_EMAIL, email)
        self.click(self.SUBSCRIBE_BUTTON)

    def is_subscribe_success_displayed(self):
        # Verify subscription success message
        try:
            self.page.locator(self.SUBSCRIBE_SUCCESS).first.wait_for(state="visible", timeout=5000)
            return True
        except Exception:
            return False

