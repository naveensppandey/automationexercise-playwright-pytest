from pages.base_page import BasePage

class HomePage(BasePage):
    """
    HomePage represents the website home page (https://automationexercise.com/)
    and shared header/footer navigation components, including Contact Us.
    """

    URL = "https://automationexercise.com/"

    # --- Header Navigation Locators ---
    LOGO = "div.logo img"
    LOGIN_LINK = "a[href='/login']"
    PRODUCTS_LINK = "a[href='/products']"
    CART_LINK = ".shop-menu a[href='/view_cart']"
    CONTACT_US_LINK = "a[href='/contact_us']"

    # --- Footer Locators ---
    FOOTER = "#footer"
    SUBSCRIBE_EMAIL = "#susbscribe_email"
    SUBSCRIBE_BUTTON = "#subscribe"
    SUBSCRIBE_SUCCESS = "#success-subscribe, .alert-success"

    # --- Contact Us Page Locators (/contact_us) ---
    CONTACT_HEADER = "h2:has-text('GET IN TOUCH')"
    CONTACT_NAME = "input[data-qa='name']"
    CONTACT_EMAIL = "input[data-qa='email']"
    CONTACT_SUBJECT = "input[data-qa='subject']"
    CONTACT_MESSAGE = "textarea[data-qa='message']"
    CONTACT_UPLOAD_FILE = "input[name='upload_file']"
    CONTACT_SUBMIT = "input[data-qa='submit-button']"
    CONTACT_SUCCESS = ".status.alert.alert-success"

    # ==========================================
    # HOME PAGE ACTIONS
    # ==========================================

    def open(self):
        """Open the home page URL."""
        self.navigate(self.URL)

    def is_loaded(self):
        """Verify that the home page logo is visible."""
        return self.is_visible(self.LOGO)

    def click_signup_login(self):
        """Click the 'Signup / Login' link in the top menu."""
        self.click(self.LOGIN_LINK)

    def click_products(self):
        """Click the 'Products' link in the top menu."""
        self.click(self.PRODUCTS_LINK)

    def click_cart(self):
        """Click the 'Cart' link in the top menu."""
        self.click(self.CART_LINK)

    def click_contact_us(self):
        """Click the 'Contact us' link in the top menu."""
        self.click(self.CONTACT_US_LINK)

    def scroll_to_bottom(self):
        """Scroll the page down to the bottom."""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.page.wait_for_timeout(500)

    def scroll_to_top(self):
        """Scroll the page back up to the top."""
        self.page.evaluate("window.scrollTo(0, 0)")
        self.page.wait_for_timeout(500)

    def is_footer_visible(self):
        """Verify that the footer section is visible."""
        return self.is_visible(self.FOOTER)

    def subscribe(self, email):
        """Enter email in the footer subscription box and click subscribe."""
        self.fill(self.SUBSCRIBE_EMAIL, email)
        self.click(self.SUBSCRIBE_BUTTON)

    def is_subscribe_success_displayed(self):
        """Check if subscription success message is displayed."""
        return self.is_visible(self.SUBSCRIBE_SUCCESS, timeout=5000)

    # ==========================================
    # CONTACT US ACTIONS (/contact_us)
    # ==========================================

    def open_contact_us(self):
        """Open the Contact Us page directly."""
        self.navigate("https://automationexercise.com/contact_us")

    def is_contact_page_displayed(self):
        """Verify that the 'GET IN TOUCH' header is visible on Contact Us page."""
        return self.is_visible(self.CONTACT_HEADER, timeout=5000)

    def fill_contact_form(self, name, email, subject, message):
        """Fill all fields in the Contact Us form."""
        self.fill(self.CONTACT_NAME, name)
        self.fill(self.CONTACT_EMAIL, email)
        self.fill(self.CONTACT_SUBJECT, subject)
        self.fill(self.CONTACT_MESSAGE, message)

    def upload_contact_file(self, file_path):
        """Attach a file to the Contact Us form using Playwright."""
        self.page.locator(self.CONTACT_UPLOAD_FILE).set_input_files(file_path)

    def submit_contact_form(self):
        """Accept the browser confirmation dialog ('Press OK to proceed!') and submit."""
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.click(self.CONTACT_SUBMIT)

    def is_contact_success_displayed(self):
        """Verify that the contact form submission success alert is visible."""
        return self.is_visible(self.CONTACT_SUCCESS, timeout=5000)
