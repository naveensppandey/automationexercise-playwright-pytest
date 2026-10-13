import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.csv_data_provider import read_csv_data

# Valid test user credentials
VALID_EMAIL = "naveenppandey8080@gmail.com"
VALID_PASSWORD = "Np@123"

@pytest.mark.tc_id("TC01")
def test_tc01_navigate_to_login_page(page):
    """TC01: Verify navigation from Home Page to Login Page."""
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    assert home_page.is_loaded(), "Home page logo was not displayed"

    home_page.click_signup_login()
    assert login_page.is_login_page_displayed(), "Login page header was not displayed"

@pytest.mark.tc_id("TC02")
def test_tc02_valid_login_credentials(page):
    """TC02: Verify user can log in with valid credentials."""
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)

    assert login_page.is_login_successful(), "User was not logged in successfully"

@pytest.mark.tc_id("TC03")
def test_tc03_invalid_login_email(page):
    """TC03: Verify error message when logging in with invalid email."""
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login()
    login_page.login("nonexistent_user_999@test.com", VALID_PASSWORD)

    error_msg = login_page.get_error_message()
    assert "incorrect" in error_msg.lower(), f"Expected incorrect error, got: '{error_msg}'"

@pytest.mark.tc_id("TC04")
def test_tc04_invalid_login_password(page):
    """TC04: Verify error message when logging in with wrong password."""
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login()
    login_page.login(VALID_EMAIL, "WrongPassword123")

    error_msg = login_page.get_error_message()
    assert len(error_msg) > 0, "No error message was displayed for invalid password"

@pytest.mark.tc_id("TC05")
def test_tc05_blank_credentials_login(page):
    """TC05: Verify form validation requires email and password when left blank."""
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login()
    # Click login button without filling fields
    login_page.click_login()

    # Form submission is prevented by HTML5 validation, user remains on login page
    assert login_page.is_login_page_displayed(), "Should remain on login page when submitting blank fields"

@pytest.mark.tc_id("TC06")
def test_tc06_logout_functionality(page):
    """TC06: Verify user can log out and is redirected to login page."""
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    assert login_page.is_login_successful(), "User failed to log in prior to logout"

    login_page.click_logout()
    assert login_page.is_login_page_displayed(), "User was not redirected to login page after logout"

@pytest.mark.tc_id("TC07")
def test_tc07_verify_logged_in_as_header(page):
    """TC07: Verify 'Logged in as <username>' header appears after valid login."""
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)

    assert login_page.is_login_successful(), "'Logged in as' header was not visible"

@pytest.mark.tc_id("TC08")
def test_tc08_data_driven_login_user1(page):
    """TC08: Data-Driven Login Test Row 1."""
    rows = read_csv_data("test_data/login_data.csv")
    user = rows[0]
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login()
    login_page.login(user["username"], user["password"])
    assert login_page.is_login_successful(), f"Login failed for user: {user['username']}"

@pytest.mark.tc_id("TC09")
def test_tc09_data_driven_login_user2(page):
    """TC09: Data-Driven Login Test Row 2."""
    rows = read_csv_data("test_data/login_data.csv")
    user = rows[1]
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login()
    login_page.login(user["username"], user["password"])
    assert login_page.is_login_successful(), f"Login failed for user: {user['username']}"

@pytest.mark.tc_id("TC10")
def test_tc10_data_driven_login_user3(page):
    """TC10: Data-Driven Login Test Row 3."""
    rows = read_csv_data("test_data/login_data.csv")
    user = rows[2]
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login()
    login_page.login(user["username"], user["password"])
    assert login_page.is_login_successful(), f"Login failed for user: {user['username']}"

# Preserved original CSV parameterized data-driven test
@pytest.mark.parametrize("row", read_csv_data("test_data/login_data.csv"))
def test_csv_data_driven_login(page, row):
    """Original CSV data-driven parameterized test executing all rows."""
    home_page = HomePage(page)
    login_page = LoginPage(page)

    username = row["username"]
    password = row["password"]
    expected_result = row["expectedResult"]

    home_page.open()
    home_page.click_signup_login()
    login_page.login(username, password)

    if expected_result == "success":
        assert login_page.is_login_successful()
    else:
        assert len(login_page.get_error_message()) > 0
