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


def test_add_random_product_and_logout(page):
    """3-Level Random Purchase Test: Category -> Subcategory -> Product."""
    home_page = HomePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # 1. Open home page and login
    home_page.open()
    home_page.click_signup_login()
    login_page.login("naveenppandey8080@gmail.com", "Np@123")

    # 2. Go to Products page
    home_page.click_products()

    # 3. Level 1 - Select Random Category
    category_name = products_page.select_random_category()
    print(f"\n[Level 1 - Random Category]: {category_name}")

    # 4. Level 2 - Select Random Subcategory
    subcategory_name = products_page.select_random_subcategory()
    print(f"[Level 2 - Random Subcategory]: {subcategory_name}")

    # 5. Level 3 - Select Random Product
    selected_product_name = products_page.select_random_product()
    print(f"[Level 3 - Random Product]: {selected_product_name}")

    # 6. Verify product in cart
    products_page.click_view_cart_in_modal()
    assert cart_page.is_cart_page_displayed()
    assert cart_page.is_product_in_cart(selected_product_name)

    # 7. Logout
    login_page.click_logout()
    assert login_page.is_login_page_displayed()




