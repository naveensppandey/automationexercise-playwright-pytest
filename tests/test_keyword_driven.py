from utils.keyword_actions import execute_keyword

def test_keyword_driven_login_and_logout(page):
    """
    Keyword-Driven Test Example:
    Demonstrates executing test steps defined as a list of Keywords.
    """
    # Define test steps as (Keyword, Target/Selector, Value)
    keyword_steps = [
        ("OPEN", "https://automationexercise.com/", None),
        ("CLICK", "a[href='/login']", None),
        ("FILL", "input[data-qa='login-email']", "naveenppandey8080@gmail.com"),
        ("FILL", "input[data-qa='login-password']", "Np@123"),
        ("CLICK", "button[data-qa='login-button']", None),
        ("LOGOUT", None, None)
    ]

    # Execute each keyword action in order
    for step in keyword_steps:
        keyword, target, value = step
        execute_keyword(page, keyword, target, value)
