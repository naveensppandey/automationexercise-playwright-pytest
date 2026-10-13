import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.csv_data_provider import get_random_valid_user

@pytest.mark.tc_id("TC15")
def test_tc15_random_product_selection_level_3(page):
    """TC15: Random Product Selection Level 3 - dynamically pick product card."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()

    # Discover and select a random product
    product_name = products_page.select_random_product()
    print(f"\n[TC15 - Level 3 Dynamic Product Selected]: {product_name}")
    assert len(product_name) > 0, "No product name captured from dynamic card selection"

@pytest.mark.tc_id("TC26")
def test_tc26_random_category_selection_level_1(page):
    """TC26: Random Category Selection Level 1 - dynamically expand category."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()

    # Select random category
    category_name = products_page.select_random_category()
    print(f"\n[TC26 - Level 1 Dynamic Category Selected]: {category_name}")
    assert len(category_name) > 0, "No category name returned from dynamic selection"

@pytest.mark.tc_id("TC27")
def test_tc27_random_subcategory_selection_level_2(page):
    """TC27: Random Subcategory Selection Level 2 - expand category and click subcategory."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()

    category_name = products_page.select_random_category()
    subcategory_name = products_page.select_random_subcategory()
    print(f"\n[TC27 - Level 2 Dynamic Subcategory Selected]: {subcategory_name} under {category_name}")
    assert len(subcategory_name) > 0, "No subcategory name returned"

@pytest.mark.tc_id("TC28")
def test_tc28_three_level_dynamic_selection_chain(page):
    """TC28: 3-Level Dynamic Selection Chain (Category -> Subcategory -> Product)."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()

    cat = products_page.select_random_category()
    subcat = products_page.select_random_subcategory()
    prod = products_page.select_random_product()

    print(f"\n[TC28 Dynamic Chain]: Category='{cat}' -> Subcategory='{subcat}' -> Product='{prod}'")
    assert len(cat) > 0 and len(subcat) > 0 and len(prod) > 0

@pytest.mark.tc_id("TC50")
def test_tc50_complete_purchase_and_logout_flow(page):
    """
    TC50: Complete End-to-End Purchase & Logout Flow.
    Preserves the mandatory 3-level hierarchical product randomization:
    Random User Login -> Level 1 (Category) -> Level 2 (Subcategory) -> Level 3 (Product) -> Cart -> Logout.
    """
    home_page = HomePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # 1. Select random valid user from CSV and Login
    random_user = get_random_valid_user()
    print(f"\n[TC50 Random User]: {random_user['username']}")

    home_page.open()
    home_page.click_signup_login()
    login_page.login(random_user["username"], random_user["password"])
    assert login_page.is_login_successful(), f"Login failed for random user {random_user['username']}"

    # 2. Navigate to Products
    home_page.click_products()

    # 3. Level 1 - Select Random Category
    category_name = products_page.select_random_category()
    print(f"[TC50 Level 1 - Random Category]: {category_name}")
    assert len(category_name) > 0

    # 4. Level 2 - Select Random Subcategory
    subcategory_name = products_page.select_random_subcategory()
    print(f"[TC50 Level 2 - Random Subcategory]: {subcategory_name}")
    assert len(subcategory_name) > 0

    # 5. Level 3 - Select Random Product & Add to Cart
    selected_product_name = products_page.select_random_product()
    print(f"[TC50 Level 3 - Random Product]: {selected_product_name}")
    assert len(selected_product_name) > 0

    # 6. Verify in Cart
    products_page.click_view_cart_in_modal()
    assert cart_page.is_cart_page_displayed(), "Cart page was not displayed"
    assert cart_page.is_product_in_cart(selected_product_name), f"Product '{selected_product_name}' not found in cart"

    # 7. Logout
    login_page.click_logout()
    assert login_page.is_login_page_displayed(), "User was not logged out successfully"
    print("\n[TC50 Passed]: Complete E2E flow with 3-level randomization succeeded!")
