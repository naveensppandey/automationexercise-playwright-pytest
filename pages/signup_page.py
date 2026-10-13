from pages.base_page import BasePage

class SignupPage(BasePage):
    """SignupPage represents the account registration and deletion page (/signup)."""

    # Locators
    TITLE_MR = "#id_gender1"
    TITLE_MRS = "#id_gender2"
    PASSWORD_INPUT = "#password"
    DAYS_SELECT = "#days"
    MONTHS_SELECT = "#months"
    YEARS_SELECT = "#years"
    FIRST_NAME_INPUT = "#first_name"
    LAST_NAME_INPUT = "#last_name"
    ADDRESS_INPUT = "#address1"
    COUNTRY_SELECT = "#country"
    STATE_INPUT = "#state"
    CITY_INPUT = "#city"
    ZIPCODE_INPUT = "#zipcode"
    MOBILE_INPUT = "#mobile_number"
    CREATE_ACCOUNT_BTN = "button[data-qa='create-account']"
    ACCOUNT_CREATED_HEADER = "h2[data-qa='account-created']"
    CONTINUE_BTN = "a[data-qa='continue-button']"
    DELETE_ACCOUNT_LINK = "a[href='/delete_account']"
    ACCOUNT_DELETED_HEADER = "h2[data-qa='account-deleted']"

    def is_signup_page_displayed(self):
        # Verify page title or account info header
        return self.is_visible("b:has-text('Enter Account Information')")

    def select_gender_mr(self):
        # Check Mr. radio button
        self.page.locator(self.TITLE_MR).check()

    def is_gender_mr_checked(self):
        # Verify Mr. radio button is checked
        return self.page.locator(self.TITLE_MR).is_checked()

    def select_country(self, country_name="India"):
        # Select country from dropdown
        self.page.locator(self.COUNTRY_SELECT).select_option(country_name)

    def get_selected_country(self):
        # Get selected country text or value
        return self.page.locator(self.COUNTRY_SELECT).input_value()

    def fill_full_account_details(self, password="Password123"):
        # Fill all mandatory registration fields
        self.select_gender_mr()
        self.fill(self.PASSWORD_INPUT, password)
        self.fill(self.FIRST_NAME_INPUT, "Demo")
        self.fill(self.LAST_NAME_INPUT, "User")
        self.fill(self.ADDRESS_INPUT, "123 Test Street")
        self.select_country("India")
        self.fill(self.STATE_INPUT, "Maharashtra")
        self.fill(self.CITY_INPUT, "Mumbai")
        self.fill(self.ZIPCODE_INPUT, "400001")
        self.fill(self.MOBILE_INPUT, "9876543210")

    def click_create_account(self):
        # Submit registration form
        self.click(self.CREATE_ACCOUNT_BTN)

    def is_account_created_displayed(self):
        # Verify 'ACCOUNT CREATED!' header
        try:
            self.page.locator(self.ACCOUNT_CREATED_HEADER).wait_for(state="visible", timeout=5000)
            return True
        except Exception:
            return False

    def click_continue(self):
        # Click Continue button after account creation
        self.click(self.CONTINUE_BTN)

    def click_delete_account(self):
        # Click Delete Account link
        self.click(self.DELETE_ACCOUNT_LINK)

    def is_account_deleted_displayed(self):
        # Verify 'ACCOUNT DELETED!' header
        try:
            self.page.locator(self.ACCOUNT_DELETED_HEADER).wait_for(state="visible", timeout=5000)
            return True
        except Exception:
            return False
