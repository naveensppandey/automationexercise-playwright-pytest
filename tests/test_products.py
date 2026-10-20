import os
import time
import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage

# ==============================================================================
# PRODUCTS & CATALOG TEST CASES (TC11 - TC14, TC16 - TC20)
# ==============================================================================

@pytest.mark.tc_id("TC11")
def test_tc11_navigate_to_products_page(page):
    """TC11: Verify navigation to Products page."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()
    assert products_page.is_all_products_header_visible() or "products" in page.url.lower(), "Products page was not displayed"

@pytest.mark.tc_id("TC12")
def test_tc12_search_existing_product(page):
    """TC12: Search existing product 'dress' and verify results."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()
    products_page.search_product("dress")

    assert products_page.is_search_results_visible(), "Searched products header was not displayed"
    assert products_page.get_search_results_count() > 0, "No search results returned for 'dress'"

@pytest.mark.tc_id("TC13")
def test_tc13_search_nonexistent_product(page):
    """TC13: Search non-existent product and verify empty results."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()
    products_page.search_product("xyznonexistent123")

    count = products_page.get_search_results_count()
    assert count == 0, f"Expected 0 results for non-existent product, found {count}"

@pytest.mark.tc_id("TC14")
def test_tc14_view_product_details(page):
    """TC14: View product details for first catalog item."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()
    products_page.click_first_product_details()

    assert products_page.is_product_detail_displayed(), "Product detail section was not displayed"

@pytest.mark.tc_id("TC16")
def test_tc16_add_first_item_to_cart(page):
    """TC16: Add first item in catalog to cart."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()
    product_name = products_page.add_first_product_to_cart()

    assert len(product_name) > 0, "First product name was empty"

@pytest.mark.tc_id("TC17")
def test_tc17_add_second_item_to_cart(page):
    """TC17: Add second item in catalog to cart."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()
    product_name = products_page.add_second_product_to_cart()

    assert len(product_name) > 0, "Second product name was empty"

@pytest.mark.tc_id("TC18")
def test_tc18_search_product_top(page):
    """TC18: Search product 'top'."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()
    products_page.search_product("top")

    assert products_page.is_search_results_visible(), "Searched products header not displayed for 'top'"
    assert products_page.get_search_results_count() > 0, "No results returned for 'top'"

@pytest.mark.tc_id("TC19")
def test_tc19_search_product_jeans(page):
    """TC19: Search product 'jeans'."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()
    products_page.search_product("jeans")

    assert products_page.is_search_results_visible(), "Searched products header not displayed for 'jeans'"
    assert products_page.get_search_results_count() > 0, "No results returned for 'jeans'"

@pytest.mark.tc_id("TC20")
def test_tc20_verify_all_products_header(page):
    """TC20: Verify 'ALL PRODUCTS' header is visible on Products page."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()

    assert products_page.is_all_products_header_visible(), "'ALL PRODUCTS' header was not visible"

# ==============================================================================
# CATEGORY & SUBCATEGORY TEST CASES (TC21 - TC25)
# ==============================================================================

@pytest.mark.tc_id("TC21")
def test_tc21_expand_women_category(page):
    """TC21: Expand Women category in sidebar."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()
    products_page.expand_category("Women")

    assert products_page.is_category_expanded("Women"), "Women category was not expanded"

@pytest.mark.tc_id("TC22")
def test_tc22_expand_men_category(page):
    """TC22: Expand Men category in sidebar."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()
    products_page.expand_category("Men")

    assert products_page.is_category_expanded("Men"), "Men category was not expanded"

@pytest.mark.tc_id("TC23")
def test_tc23_expand_kids_category(page):
    """TC23: Expand Kids category in sidebar."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()
    products_page.expand_category("Kids")

    assert products_page.is_category_expanded("Kids"), "Kids category was not expanded"

@pytest.mark.tc_id("TC24")
def test_tc24_select_women_dress_subcategory(page):
    """TC24: Select Women -> Dress subcategory."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()
    products_page.select_subcategory_by_name("Women", "Dress")

    header_text = page.locator("h2.title.text-center").first.inner_text().strip()
    assert "women" in header_text.lower() or "dress" in header_text.lower(), f"Unexpected header: {header_text}"

@pytest.mark.tc_id("TC25")
def test_tc25_select_men_tshirts_subcategory(page):
    """TC25: Select Men -> Tshirts subcategory."""
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.open()
    home_page.click_products()
    products_page.select_subcategory_by_name("Men", "Tshirts")

    header_text = page.locator("h2.title.text-center").first.inner_text().strip()
    assert "men" in header_text.lower() or "tshirt" in header_text.lower(), f"Unexpected header: {header_text}"

# ==============================================================================
# CONTACT US TEST CASES (TC44 - TC46)
# ==============================================================================

@pytest.mark.tc_id("TC44")
def test_tc44_navigate_to_contact_us_page(page):
    """TC44: Navigate to Contact Us page."""
    home_page = HomePage(page)

    home_page.open()
    home_page.click_contact_us()

    assert home_page.is_contact_page_displayed() or "contact_us" in page.url.lower(), "Contact Us page not displayed"

@pytest.mark.tc_id("TC45")
def test_tc45_submit_contact_us_form(page):
    """TC45: Submit Contact Us form and verify success message."""
    home_page = HomePage(page)

    home_page.open_contact_us()
    home_page.fill_contact_form(
        name="Student Demo",
        email="student_demo@test.com",
        subject="Project Inquiry",
        message="This is a test message from our automated Playwright framework."
    )
    home_page.submit_contact_form()

    assert home_page.is_contact_success_displayed(), "Contact submission success message not displayed"

@pytest.mark.tc_id("TC46")
def test_tc46_upload_file_in_contact_us(page):
    """TC46: Attach file and submit Contact Us form."""
    home_page = HomePage(page)
    sample_file = os.path.abspath("test_data/sample_upload.txt")

    home_page.open_contact_us()
    home_page.fill_contact_form(
        name="Upload User",
        email="upload_user@test.com",
        subject="File Upload Verification",
        message="Testing file upload capability."
    )
    home_page.upload_contact_file(sample_file)
    home_page.submit_contact_form()

    assert home_page.is_contact_success_displayed(), "Success message after file upload not displayed"

# ==============================================================================
# HOME PAGE TEST CASES (TC47 - TC49)
# ==============================================================================

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
