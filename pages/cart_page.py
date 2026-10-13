from pages.base_page import BasePage

class CartPage(BasePage):
    """CartPage represents the shopping cart view page."""

    # Page Locators
    CART_TABLE = "#cart_info_table"
    CART_PRODUCT_NAMES = "td.cart_description h4 a"
    CHECKOUT_BUTTON = "a.check_out"

    def is_cart_page_displayed(self):
        # Wait up to 10s for cart table to appear on page load
        try:
            self.page.locator("#cart_info_table, #cart_items").first.wait_for(state="visible", timeout=10000)
            return True
        except Exception:
            return False

    def is_product_in_cart(self, product_name):
        # Check if product_name is present in cart table rows
        try:
            self.page.locator("#cart_info_table tbody tr").first.wait_for(state="visible", timeout=10000)
            rows = self.page.locator("#cart_info_table tbody tr").all_inner_texts()
            for row_text in rows:
                if product_name.lower() in row_text.lower():
                    return True
        except Exception:
            pass
        return False

    def click_proceed_to_checkout(self):
        # Click Proceed to Checkout button
        self.click(self.CHECKOUT_BUTTON)

    def get_table_headers(self):
        # Get list of header texts from cart table
        return self.page.locator("#cart_info_table thead td").all_inner_texts()

    def get_product_quantity(self, product_name):
        # Get quantity value for a given product in cart table
        row = self.page.locator(f"#cart_info_table tr:has-text('{product_name}')")
        return row.locator("td.cart_quantity button").inner_text().strip()

    def is_empty_cart_displayed(self):
        # Check if empty cart notification or empty table is displayed
        return self.is_visible("#empty_cart") or self.page.locator("#cart_info_table tbody tr").count() == 0

