from pages.base_page import BasePage

class ContactUsPage(BasePage):
    """ContactUsPage represents the contact us form (/contact_us)."""

    URL = "https://automationexercise.com/contact_us"

    # Locators
    CONTACT_HEADER = "h2:has-text('GET IN TOUCH')"
    NAME_INPUT = "input[data-qa='name']"
    EMAIL_INPUT = "input[data-qa='email']"
    SUBJECT_INPUT = "input[data-qa='subject']"
    MESSAGE_INPUT = "textarea[data-qa='message']"
    UPLOAD_FILE_INPUT = "input[name='upload_file']"
    SUBMIT_BTN = "input[data-qa='submit-button']"
    SUCCESS_ALERT = ".status.alert.alert-success"
    HOME_BTN = "a.btn.btn-success[href='/']"

    def open(self):
        # Open Contact Us page directly
        self.navigate(self.URL)

    def is_contact_page_displayed(self):
        # Check if GET IN TOUCH header is visible
        return self.is_visible(self.CONTACT_HEADER)

    def fill_contact_form(self, name, email, subject, message):
        # Fill name, email, subject, and message
        self.fill(self.NAME_INPUT, name)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.SUBJECT_INPUT, subject)
        self.fill(self.MESSAGE_INPUT, message)

    def upload_file(self, file_path):
        # Attach file using Playwright set_input_files
        self.page.locator(self.UPLOAD_FILE_INPUT).set_input_files(file_path)

    def submit_form(self):
        # Accept the confirmation alert popup and click submit
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.click(self.SUBMIT_BTN)

    def is_success_message_displayed(self):
        # Verify submission success alert is visible
        try:
            self.page.locator(self.SUCCESS_ALERT).wait_for(state="visible", timeout=5000)
            return True
        except Exception:
            return False

    def get_success_message(self):
        # Get success alert text
        return self.get_text(self.SUCCESS_ALERT)
