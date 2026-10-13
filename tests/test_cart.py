import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.mark.tc_id("TC29")
def test_tc29_open_cart_via_navbar(page):
    """TC29: Open Cart page via top navigation bar."""
    home_page = HomePage(page)
    cart_page = CartPage(page)

    home_page.open()
    home_page.click_cart()

    assert cart_page.is_cart_page_displayed() or "view_cart" in page.url.lower(), "Cart page was not displayed"

@pytest.mark.tc_id("TC30")
def test_tc30_open_cart_via_modal_popup(page):
    """TC30: Add item and open cart via modal popup."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    home_page.open()
    home_page.click_products()
    product_name = products_page.add_first_product_to_cart()
    products_page.click_view_cart_in_modal()

    assert cart_page.is_cart_page_displayed(), "Cart page was not displayed"
    assert cart_page.is_product_in_cart(product_name), f"Product '{product_name}' not in cart"

@pytest.mark.tc_id("TC31")
def test_tc31_verify_product_name_in_cart(page):
    """TC31: Verify added product name appears in cart table."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    home_page.open()
    home_page.click_products()
    product_name = products_page.add_first_product_to_cart()
    products_page.click_view_cart_in_modal()

    assert cart_page.is_product_in_cart(product_name), f"Expected '{product_name}' in cart"

@pytest.mark.tc_id("TC32")
def test_tc32_verify_cart_table_headers(page):
    """TC32: Verify headers in cart info table."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    home_page.open()
    home_page.click_products()
    products_page.add_first_product_to_cart()
    products_page.click_view_cart_in_modal()

    headers = cart_page.get_table_headers()
    headers_text = " ".join(headers).lower()
    for expected_header in ["item", "description", "price", "quantity"]:
        assert expected_header in headers_text, f"Header '{expected_header}' missing from {headers}"

@pytest.mark.tc_id("TC33")
def test_tc33_proceed_to_checkout_button(page):
    """TC33: Verify clicking Proceed to Checkout button."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    home_page.open()
    home_page.click_products()
    products_page.add_first_product_to_cart()
    products_page.click_view_cart_in_modal()

    cart_page.click_proceed_to_checkout()
    # If not logged in, modal with 'Register / Login' appears, or checkout page opens
    assert page.locator(".modal-content, #checkoutModal, #address_delivery").first.is_visible() or "checkout" in page.url or "login" in page.url

@pytest.mark.tc_id("TC34")
def test_tc34_verify_quantity_in_cart(page):
    """TC34: Verify default quantity in cart is 1."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    home_page.open()
    home_page.click_products()
    product_name = products_page.add_first_product_to_cart()
    products_page.click_view_cart_in_modal()

    qty = cart_page.get_product_quantity(product_name)
    assert qty == "1", f"Expected quantity '1', got '{qty}'"

@pytest.mark.tc_id("TC35")
def test_tc35_empty_cart_navigation(page):
    """TC35: Navigate to cart with empty session and verify empty notice or table."""
    home_page = HomePage(page)
    cart_page = CartPage(page)

    home_page.open()
    home_page.click_cart()

    assert cart_page.is_empty_cart_displayed() or cart_page.is_cart_page_displayed()

@pytest.mark.tc_id("TC36")
def test_tc36_multiple_products_in_cart(page):
    """TC36: Add multiple products to cart and verify both exist."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    home_page.open()
    home_page.click_products()
    p1 = products_page.add_first_product_to_cart()
    p2 = products_page.add_second_product_to_cart()
    products_page.click_view_cart_in_modal()

    assert cart_page.is_product_in_cart(p1), f"First product '{p1}' missing from cart"
    assert cart_page.is_product_in_cart(p2), f"Second product '{p2}' missing from cart"
