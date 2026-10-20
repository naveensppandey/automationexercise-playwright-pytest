from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    LoginPage represents the Signup / Login page (https://automationexercise.com/login).
    It manages both user login and user registration (signup) forms.
    """

    # --- Login Form Locators ---
    LOGIN_HEADER = ".login-form h2"
    EMAIL_INPUT = "input[data-qa='login-email']"
    PASSWORD_INPUT = "input[data-qa='login-password']"
    LOGIN_BUTTON = "button[data-qa='login-button']"
    LOGGED_IN_TEXT = "a:has-text('Logged in as')"
    LOGOUT_LINK = "a[href='/logout']"
    ERROR_MESSAGE = ".login-form p"

    # --- Initial Signup Form Locators ---
    SIGNUP_HEADER = ".signup-form h2"
    SIGNUP_NAME_INPUT = "input[data-qa='signup-name']"
    SIGNUP_EMAIL_INPUT = "input[data-qa='signup-email']"
    SIGNUP_BUTTON = "button[data-qa='signup-button']"
    SIGNUP_ERROR_MESSAGE = ".signup-form p"

    # --- Detailed Registration Form Locators (/signup) ---
    GENDER_MR_RADIO = "#id_gender1"
    ACCOUNT_PASSWORD_INPUT = "#password"
    FIRST_NAME_INPUT = "#first_name"
    LAST_NAME_INPUT = "#last_name"
    ADDRESS_INPUT = "#address1"
    COUNTRY_SELECT = "#country"
    STATE_INPUT = "#state"
    CITY_INPUT = "#city"
    ZIPCODE_INPUT = "#zipcode"
    MOBILE_INPUT = "#mobile_number"
    CREATE_ACCOUNT_BUTTON = "button[data-qa='create-account']"
    ACCOUNT_CREATED_HEADER = "h2[data-qa='account-created']"
    CONTINUE_BUTTON = "a[data-qa='continue-button']"
    DELETE_ACCOUNT_LINK = "a[href='/delete_account']"
    ACCOUNT_DELETED_HEADER = "h2[data-qa='account-deleted']"

    # ==========================================
    # LOGIN METHODS
    # ==========================================

    def is_login_page_displayed(self):
        """Check if 'Login to your account' header is visible."""
        return self.is_visible(self.LOGIN_HEADER)

    def enter_email(self, email):
        """Type email into the login input field."""
        self.fill(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Type password into the login input field."""
        self.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click the Login button."""
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        """Convenience method to fill credentials and click login."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self):
        """Check if 'Logged in as <username>' text appears in the top navigation."""
        return self.is_visible(self.LOGGED_IN_TEXT, timeout=5000)

    def get_error_message(self):
        """Get the error message text displayed on login failure."""
        if self.is_visible(self.ERROR_MESSAGE, timeout=5000):
            return self.get_text(self.ERROR_MESSAGE)
        return ""

    def click_logout(self):
        """Click the Logout button in the top navigation."""
        self.click(self.LOGOUT_LINK)

    # ==========================================
    # SIGNUP & REGISTRATION METHODS
    # ==========================================

    def signup_initial(self, name, email):
        """Fill name and email under 'New User Signup!' and click Signup."""
        self.fill(self.SIGNUP_NAME_INPUT, name)
        self.fill(self.SIGNUP_EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)

    def get_signup_error_message(self):
        """Get the error message text under the signup form (e.g., email already exists)."""
        if self.is_visible(self.SIGNUP_ERROR_MESSAGE, timeout=5000):
            return self.get_text(self.SIGNUP_ERROR_MESSAGE)
        return ""

    def is_signup_details_page_displayed(self):
        """Check if 'ENTER ACCOUNT INFORMATION' header is visible on /signup."""
        return self.is_visible("b:has-text('Enter Account Information')")

    def select_gender_mr(self):
        """Select the 'Mr.' gender radio button."""
        self.page.locator(self.GENDER_MR_RADIO).check()

    def is_gender_mr_checked(self):
        """Verify if the 'Mr.' gender radio button is checked."""
        return self.page.locator(self.GENDER_MR_RADIO).is_checked()

    def select_country(self, country_name="India"):
        """Select a country from the dropdown."""
        self.page.locator(self.COUNTRY_SELECT).select_option(country_name)

    def get_selected_country(self):
        """Return the currently selected country value."""
        return self.page.locator(self.COUNTRY_SELECT).input_value()

    def fill_registration_details(self, password="Password123!"):
        """Fill all mandatory account details on the registration form."""
        self.select_gender_mr()
        self.fill(self.ACCOUNT_PASSWORD_INPUT, password)
        self.fill(self.FIRST_NAME_INPUT, "Demo")
        self.fill(self.LAST_NAME_INPUT, "User")
        self.fill(self.ADDRESS_INPUT, "123 Marine Drive")
        self.select_country("India")
        self.fill(self.STATE_INPUT, "Maharashtra")
        self.fill(self.CITY_INPUT, "Mumbai")
        self.fill(self.ZIPCODE_INPUT, "400001")
        self.fill(self.MOBILE_INPUT, "9876543210")

    def click_create_account(self):
        """Click the 'Create Account' button."""
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def is_account_created_displayed(self):
        """Check if 'ACCOUNT CREATED!' success header is visible."""
        return self.is_visible(self.ACCOUNT_CREATED_HEADER, timeout=5000)

    def click_continue(self):
        """Click the Continue button after account creation."""
        self.click(self.CONTINUE_BUTTON)

    def click_delete_account(self):
        """Click the 'Delete Account' link in the top navigation."""
        self.click(self.DELETE_ACCOUNT_LINK)

    def is_account_deleted_displayed(self):
        """Check if 'ACCOUNT DELETED!' success header is visible."""
        return self.is_visible(self.ACCOUNT_DELETED_HEADER, timeout=5000)
