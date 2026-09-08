from pages.base_page import BasePage

class CartPage(BasePage):
    """CartPage represents the shopping cart view page."""

    # Page Locators
    CART_TABLE = "#cart_info_table"
    CART_PRODUCT_NAMES = "td.cart_description h4 a"
    CHECKOUT_BUTTON = "a.check_out"

    def is_cart_page_displayed(self):
        # Wait up to 5s for cart table to appear on page load
        try:
            self.page.locator(self.CART_TABLE).wait_for(state="visible", timeout=5000)
            return True
        except Exception:
            return False

    def is_product_in_cart(self, product_name):
        # Get text of all items in cart and check if product_name is in list
        names = self.page.locator(self.CART_PRODUCT_NAMES).all_inner_texts()
        for name in names:
            if product_name.lower() in name.lower():
                return True
        return False

    def click_proceed_to_checkout(self):
        # Click Proceed to Checkout button
        self.click(self.CHECKOUT_BUTTON)
