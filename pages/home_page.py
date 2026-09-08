from pages.base_page import BasePage

class HomePage(BasePage):
    """HomePage represents the home page (https://automationexercise.com/)."""

    URL = "https://automationexercise.com/"

    # Page Locators
    LOGO = "div.logo img"
    LOGIN_LINK = "a[href='/login']"
    PRODUCTS_LINK = "a[href='/products']"
    CART_LINK = "a[href='/view_cart']"

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
