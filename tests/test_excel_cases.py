import os
import time
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.contact_us_page import ContactUsPage

EXISTING_EMAIL = "naveenppandey8080@gmail.com"

@pytest.mark.tc_id("TC37")
def test_tc37_new_user_signup_initial_step(page):
    """TC37: New User Signup Initial Step navigation to account info page."""
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

    home_page.open()
    home_page.click_signup_login()
    temp_email = f"auto_{int(time.time())}@example.com"
    login_page.signup_initial("Test User", temp_email)

    assert signup_page.is_signup_page_displayed() or "signup" in page.url.lower(), "Account info page not displayed"

@pytest.mark.tc_id("TC38")
def test_tc38_signup_existing_email_error(page):
    """TC38: Verify error message when signing up with existing email."""
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login()
    login_page.signup_initial("Existing User", EXISTING_EMAIL)

    error_msg = login_page.get_signup_error_message()
    assert "already exist" in error_msg.lower(), f"Expected already exist error, got: '{error_msg}'"

@pytest.mark.tc_id("TC39")
def test_tc39_verify_account_created_message(page):
    """TC39: Complete registration form and verify 'ACCOUNT CREATED!' message."""
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

    home_page.open()
    home_page.click_signup_login()
    temp_email = f"user_reg_{int(time.time())}@test.com"
    login_page.signup_initial("Reg User", temp_email)

    signup_page.fill_full_account_details("Password123!")
    signup_page.click_create_account()

    assert signup_page.is_account_created_displayed(), "'ACCOUNT CREATED!' message was not displayed"

@pytest.mark.tc_id("TC40")
def test_tc40_delete_account_flow(page):
    """TC40: Complete registration then execute Delete Account flow."""
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

    home_page.open()
    home_page.click_signup_login()
    temp_email = f"del_user_{int(time.time())}@test.com"
    login_page.signup_initial("Del User", temp_email)

    signup_page.fill_full_account_details("Password123!")
    signup_page.click_create_account()
    signup_page.click_continue()

    signup_page.click_delete_account()
    assert signup_page.is_account_deleted_displayed(), "'ACCOUNT DELETED!' message was not displayed"

@pytest.mark.tc_id("TC41")
def test_tc41_mandatory_field_validation(page):
    """TC41: Verify validation when submitting signup with blank fields."""
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login()
    # Click signup with blank name and email
    login_page.click(login_page.SIGNUP_BUTTON)

    # Browser HTML5 validation prevents submission; page remains on login page
    assert login_page.is_login_page_displayed(), "Should remain on login page when submitting blank signup"

@pytest.mark.tc_id("TC42")
def test_tc42_country_dropdown_selection(page):
    """TC42: Verify Country dropdown selection in signup form."""
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

    home_page.open()
    home_page.click_signup_login()
    temp_email = f"cntry_{int(time.time())}@test.com"
    login_page.signup_initial("Country User", temp_email)

    signup_page.select_country("India")
    val = signup_page.get_selected_country()
    assert val.lower() == "india", f"Expected country 'India', got '{val}'"

@pytest.mark.tc_id("TC43")
def test_tc43_gender_radio_button(page):
    """TC43: Verify Gender 'Mr.' radio button selection."""
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

    home_page.open()
    home_page.click_signup_login()
    temp_email = f"gender_{int(time.time())}@test.com"
    login_page.signup_initial("Gender User", temp_email)

    signup_page.select_gender_mr()
    assert signup_page.is_gender_mr_checked(), "Gender 'Mr.' radio button was not checked"

@pytest.mark.tc_id("TC44")
def test_tc44_navigate_to_contact_us_page(page):
    """TC44: Navigate to Contact Us page."""
    home_page = HomePage(page)
    contact_page = ContactUsPage(page)

    home_page.open()
    home_page.click_contact_us()

    assert contact_page.is_contact_page_displayed() or "contact_us" in page.url.lower(), "Contact Us page not displayed"

@pytest.mark.tc_id("TC45")
def test_tc45_submit_contact_us_form(page):
    """TC45: Submit Contact Us form and verify success message."""
    contact_page = ContactUsPage(page)

    contact_page.open()
    contact_page.fill_contact_form(
        name="Automation User",
        email="auto_contact@test.com",
        subject="Inquiry regarding Automation Project",
        message="This is an automated test message from Playwright test suite."
    )
    contact_page.submit_form()

    assert contact_page.is_success_message_displayed(), "Contact submission success message not displayed"

@pytest.mark.tc_id("TC46")
def test_tc46_upload_file_in_contact_us(page):
    """TC46: Attach file and submit Contact Us form."""
    contact_page = ContactUsPage(page)
    sample_file = os.path.abspath("test_data/sample_upload.txt")

    contact_page.open()
    contact_page.fill_contact_form(
        name="File Upload User",
        email="file_contact@test.com",
        subject="File Upload Attachment Test",
        message="Testing file upload capability."
    )
    contact_page.upload_file(sample_file)
    contact_page.submit_form()

    assert contact_page.is_success_message_displayed(), "Success message after file upload not displayed"

@pytest.mark.tc_id("TC47")
def test_tc47_verify_home_page_logo(page):
    """TC47: Verify Home Page logo visibility."""
    home_page = HomePage(page)

    home_page.open()
    assert home_page.is_loaded(), "Home page logo was not visible"

@pytest.mark.tc_id("TC48")
def test_tc48_scroll_to_bottom_and_top(page):
    """TC48: Scroll to bottom and back to top of Home Page."""
    home_page = HomePage(page)

    home_page.open()
    home_page.scroll_to_bottom()
    assert home_page.is_footer_visible(), "Footer not visible after scrolling to bottom"

    home_page.scroll_to_top()
    assert home_page.is_loaded(), "Header logo not visible after scrolling to top"

@pytest.mark.tc_id("TC49")
def test_tc49_subscription_form_in_footer(page):
    """TC49: Enter email in footer subscription form."""
    home_page = HomePage(page)

    home_page.open()
    home_page.scroll_to_bottom()
    temp_email = f"sub_{int(time.time())}@subscribe.com"
    home_page.subscribe(temp_email)

    assert home_page.is_subscribe_success_displayed(), "Subscription success message not displayed"
