from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_search_and_add_product_to_cart(page):
    """End-to-End Test: Search for product, add to cart, and verify in cart."""
    # 1. Initialize Page Objects
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # 2. Open home page and click Products link
    home_page.open()
    home_page.click_products()

    # 3. Search for product 'dress'
    products_page.search_product("dress")
    assert products_page.is_search_results_visible()

    # 4. Add product to cart and click View Cart
    products_page.add_first_product_to_cart()
    products_page.click_view_cart_in_modal()

    # 5. Verify product is in cart and click proceed to checkout
    assert cart_page.is_cart_page_displayed()
    assert cart_page.is_product_in_cart("dress")
    cart_page.click_proceed_to_checkout()


def test_add_blue_top_and_logout(page):
    """
    Test Case: Login with naveenppandey8080@gmail.com, search 'Blue Top',
    add to cart, proceed to cart, and logout.
    """
    home_page = HomePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # Step 1: Open Home page and login with naveenppandey8080@gmail.com
    home_page.open()
    home_page.click_signup_login()
    login_page.login("naveenppandey8080@gmail.com", "Np@123")

    # Step 2: Go to Products page & search 'Blue Top'
    home_page.click_products()
    products_page.search_product("Blue Top")
    assert products_page.is_search_results_visible()

    # Step 3: Add 'Blue Top' to cart
    products_page.add_first_product_to_cart()
    products_page.click_view_cart_in_modal()

    # Step 4: Verify 'Blue Top' is in cart section
    assert cart_page.is_cart_page_displayed()
    assert cart_page.is_product_in_cart("Blue Top")

    # Step 5: Log out
    login_page.click_logout()
    assert login_page.is_login_page_displayed()
