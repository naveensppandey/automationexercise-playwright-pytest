import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.csv_data_provider import read_csv_data

def test_login_page_navigation(page):
    """Test Case 1: Verify navigating from Home to Login page."""
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    assert home_page.is_loaded()

    home_page.click_signup_login()
    assert login_page.is_login_page_displayed()


def test_invalid_login(page):
    """Test Case 2: Verify login with invalid credentials shows error."""
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.click_signup_login()
    login_page.login("wrong_user@gmail.com", "wrongpass123")

    error_msg = login_page.get_error_message()
    assert len(error_msg) > 0


# Test Case 3: Data-Driven Login Test reading from login_data.csv
@pytest.mark.parametrize("row", read_csv_data("test_data/login_data.csv"))
def test_csv_data_driven_login(page, row):
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

