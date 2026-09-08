from pages.base_page import BasePage

class LoginPage(BasePage):
    """LoginPage represents the Signup / Login page."""

    # Page Locators
    EMAIL_INPUT = "input[data-qa='login-email']"
    PASSWORD_INPUT = "input[data-qa='login-password']"
    LOGIN_BUTTON = "button[data-qa='login-button']"
    LOGIN_HEADER = ".login-form h2"
    LOGGED_IN_TEXT = "a:has-text('Logged in as')"
    LOGOUT_LINK = "a[href='/logout']"
    ERROR_MESSAGE = ".login-form p"

    def is_login_page_displayed(self):
        # Verify 'Login to your account' header is visible
        return self.is_visible(self.LOGIN_HEADER)

    def enter_email(self, email):
        # Type email into input field
        self.fill(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        # Type password into input field
        self.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        # Click login button
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        # Convenience method to fill credentials and click login
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self):
        # Wait up to 5s for 'Logged in as <user>' text to appear
        try:
            self.page.locator(self.LOGGED_IN_TEXT).wait_for(state="visible", timeout=5000)
            return True
        except Exception:
            return False

    def get_error_message(self):
        # Wait up to 5s for login error message to appear
        try:
            self.page.locator(self.ERROR_MESSAGE).wait_for(state="visible", timeout=5000)
            return self.get_text(self.ERROR_MESSAGE)
        except Exception:
            return ""

    def click_logout(self):
        # Click logout link in top navbar
        self.click(self.LOGOUT_LINK)
