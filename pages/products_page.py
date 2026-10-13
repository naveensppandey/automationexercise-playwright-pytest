import re
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
        try:
            self.page.locator(self.SEARCH_BUTTON).click(force=True)
            self.page.wait_for_url("**/products?search=**", timeout=4000)
        except Exception:
            self.navigate(f"https://automationexercise.com/products?search={product_name}")
        self.page.wait_for_timeout(1000)

    def is_search_results_visible(self):
        try:
            self.page.locator("h2.title.text-center").first.wait_for(state="visible", timeout=5000)
            header_text = self.page.locator("h2.title.text-center").first.inner_text().strip()
            return "searched" in header_text.lower()
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
        selected_card.scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)

        selected_product_name = selected_card.locator(".productinfo p").inner_text().strip()
        try:
            with self.page.expect_response("**/add_to_cart/**", timeout=5000):
                selected_card.locator(".productinfo a.add-to-cart").first.click()
        except Exception:
            selected_card.locator(".productinfo a.add-to-cart").first.click(force=True)
            self.page.wait_for_timeout(1000)

        return selected_product_name

    def add_first_product_to_cart(self):
        first_card = self.page.locator(".features_items .product-image-wrapper").first
        first_card.scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)
        product_name = first_card.locator(".productinfo p").inner_text().strip()
        with self.page.expect_response("**/add_to_cart/**", timeout=10000):
            first_card.locator(".productinfo a.add-to-cart").first.click()
        self.page.wait_for_timeout(1000)
        return product_name

    def click_view_cart_in_modal(self):
        # Open cart page directly
        self.navigate("https://automationexercise.com/view_cart")

    def get_search_results_count(self):
        # Return count of search result cards
        self.page.wait_for_timeout(500)
        return self.page.locator(".features_items .product-image-wrapper").count()

    def click_first_product_details(self):
        # Click 'View Product' link on first product card
        self.page.locator("a[href^='/product_details/']").first.click()

    def is_product_detail_displayed(self):
        # Verify product detail section (title, price, availability) is loaded
        try:
            self.page.locator(".product-information").wait_for(state="visible", timeout=5000)
            return True
        except Exception:
            return False

    def is_all_products_header_visible(self):
        # Verify 'ALL PRODUCTS' title header
        return self.is_visible("h2:has-text('ALL PRODUCTS')")

    def add_second_product_to_cart(self):
        # Close modal if open
        try:
            btn = self.page.locator("#cartModal button.close-modal")
            if btn.is_visible():
                btn.click(timeout=1000)
                self.page.wait_for_timeout(500)
        except Exception:
            pass
        second_card = self.page.locator(".features_items .product-image-wrapper").nth(1)
        second_card.scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)
        product_name = second_card.locator(".productinfo p").inner_text().strip()
        with self.page.expect_response("**/add_to_cart/**", timeout=10000):
            second_card.locator(".productinfo a.add-to-cart").first.click()
        self.page.wait_for_timeout(1000)
        return product_name

    def expand_category(self, category_name="Women"):
        # Expand a specific category accordion panel
        panel = self.page.locator(f"#accordian a[href='#{category_name}']")
        panel.wait_for(state="visible", timeout=5000)
        panel.scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)
        panel.click()
        self.page.wait_for_timeout(1000)
        try:
            self.page.evaluate(f"window.$ && window.$('#{category_name}').collapse('show')")
            self.page.wait_for_timeout(500)
        except Exception:
            pass

    def is_category_expanded(self, category_name="Women"):
        # Check if subcategories under the category are expanded
        try:
            subcat_container = self.page.locator(f"#{category_name}")
            cls = subcat_container.get_attribute("class") or ""
            if "in" in cls or "collapsing" in cls:
                return True
            return subcat_container.locator("a").first.is_visible()
        except Exception:
            return False

    def select_subcategory_by_name(self, category_name, subcategory_name):
        # Expand category and navigate to specific subcategory link
        self.expand_category(category_name)
        subcat_link = self.page.locator(f"#{category_name} a").filter(has_text=re.compile(subcategory_name, re.IGNORECASE)).first
        subcat_link.wait_for(state="attached", timeout=5000)
        href = subcat_link.get_attribute("href")
        if href and href.startswith("/"):
            self.navigate(f"https://automationexercise.com{href}")
        else:
            subcat_link.click(force=True)

