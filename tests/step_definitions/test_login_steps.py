import os
from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.login_page import LoginPage

# Absolute path to features/login.feature
FEATURE_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "features",
    "login.feature"
)
scenarios(FEATURE_FILE)

@given("I open the AutomationExercise website")
def open_website(page):
    home_page = HomePage(page)
    home_page.open()

@when("I navigate to the login page")
def navigate_to_login(page):
    home_page = HomePage(page)
    home_page.click_signup_login()

@when("I enter valid login credentials")
def enter_credentials(page):
    login_page = LoginPage(page)
    login_page.enter_email("naveenppandey8080@gmail.com")
    login_page.enter_password("Np@123")

@when("I click the login button")
def click_login(page):
    login_page = LoginPage(page)
    login_page.click_login()

@then("I should be logged in successfully")
def verify_login(page):
    login_page = LoginPage(page)
    assert login_page.is_login_successful()
