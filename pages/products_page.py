from pages.base_page import BasePage

class ProductsPage(BasePage):
    """ProductsPage represents product search and catalog page."""

    # Page Locators
    SEARCH_INPUT = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    SEARCH_HEADER = "h2.title.text-center"
    PRODUCT_CARDS = ".product-image-wrapper"
    ADD_TO_CART_BUTTON = ".product-overlay a.add-to-cart, .productinfo a.add-to-cart"
    VIEW_CART_LINK = ".modal-content a[href='/view_cart']"

    def search_product(self, product_name):
        # Type search term and click search button
        self.fill(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def is_search_results_visible(self):
        # Wait up to 5 seconds for 'SEARCHED PRODUCTS' title to appear
        try:
            self.page.locator(self.SEARCH_HEADER).wait_for(state="visible", timeout=5000)
            return True
        except Exception:
            return False

    def add_first_product_to_cart(self):
        # Click add to cart on first product card
        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()

    def click_view_cart_in_modal(self):
        # Wait for pop-up modal to appear, then click 'View Cart'
        self.page.locator(self.VIEW_CART_LINK).wait_for(state="visible", timeout=5000)
        self.click(self.VIEW_CART_LINK)
