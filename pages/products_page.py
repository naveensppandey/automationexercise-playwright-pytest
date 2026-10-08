import random
from pages.base_page import BasePage

class ProductsPage(BasePage):
    """ProductsPage represents product search, category navigation, and catalog page."""

    # Page Locators
    SEARCH_INPUT = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    SEARCH_HEADER = "h2.title.text-center"
    CATEGORY_PANELS = "#accordian .panel"
    PRODUCT_CARDS = ".product-image-wrapper"
    ADD_TO_CART_BUTTON = ".productinfo a.add-to-cart"
    VIEW_CART_LINK = ".modal-content a[href='/view_cart']"

    def search_product(self, product_name):
        self.fill(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)
        self.page.wait_for_timeout(1000)

    def is_search_results_visible(self):
        try:
            self.page.locator("h2.title.text-center").first.wait_for(state="visible", timeout=5000)
            header_text = self.page.locator("h2.title.text-center").first.inner_text().strip()
            return "searched" in header_text.lower() or "product" in header_text.lower()
        except Exception:
            return False

    def select_random_category(self):
        """Level 1: Discovers top-level categories, selects one randomly, and clicks it."""
        self.page.locator(self.CATEGORY_PANELS).first.wait_for(state="visible", timeout=5000)

        panels = self.page.locator(self.CATEGORY_PANELS)
        count = panels.count()

        random_index = random.randint(0, count - 1)
        selected_panel = panels.nth(random_index)

        category_name = selected_panel.locator(".panel-title a").inner_text().strip()
        selected_panel.locator(".panel-title a").click()

        self.selected_category_panel = selected_panel
        return category_name

    def select_random_subcategory(self):
        """Level 2: Discovers subcategories under the selected category and clicks one randomly."""
        subcat_links = self.selected_category_panel.locator(".panel-collapse a")
        self.page.wait_for_timeout(500)
        count = subcat_links.count()

        random_index = random.randint(0, max(0, count - 1))
        selected_subcat = subcat_links.nth(random_index)
        subcategory_name = selected_subcat.inner_text().strip()

        href = selected_subcat.get_attribute("href")
        if href and href.startswith("/"):
            self.navigate(f"https://automationexercise.com{href}")
        else:
            selected_subcat.click(force=True)

        return subcategory_name

    def select_random_product(self):
        """Level 3: Discovers products on the page, selects one randomly, adds to cart, and returns its name."""
        self.page.locator(self.PRODUCT_CARDS).first.wait_for(state="visible", timeout=5000)

        cards = self.page.locator(self.PRODUCT_CARDS)
        count = cards.count()

        random_index = random.randint(0, max(0, count - 1))
        selected_card = cards.nth(random_index)

        selected_product_name = selected_card.locator(".productinfo p").inner_text().strip()
        with self.page.expect_response("**/add_to_cart/**", timeout=10000):
            selected_card.locator(".productinfo a.add-to-cart").first.click(force=True)

        return selected_product_name

    def add_first_product_to_cart(self):
        first_card = self.page.locator(".features_items .product-image-wrapper").first
        first_card.wait_for(state="visible", timeout=5000)
        product_name = first_card.locator(".productinfo p").inner_text().strip()
        first_card.locator(".productinfo a.add-to-cart").first.click()
        self.page.wait_for_timeout(2000)
        return product_name

    def click_view_cart_in_modal(self):
        self.navigate("https://automationexercise.com/view_cart")




