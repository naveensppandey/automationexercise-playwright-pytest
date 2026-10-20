import re
import random
from pages.base_page import BasePage

class ProductsPage(BasePage):
    """
    ProductsPage represents the catalog, product search, category navigation,
    and 3-level hierarchical product randomization.
    """

    # --- Locators ---
    SEARCH_INPUT = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    SEARCH_HEADER = "h2.title.text-center"
    CATEGORY_PANELS = "#accordian .panel"
    PRODUCT_CARDS = ".features_items .product-image-wrapper"
    ALL_PRODUCTS_HEADER = "h2:has-text('ALL PRODUCTS')"

    # ==========================================
    # SEARCH & PRODUCT DETAILS
    # ==========================================

    def search_product(self, product_name):
        """Type product name in the search box and submit."""
        self.fill(self.SEARCH_INPUT, product_name)
        try:
            self.page.locator(self.SEARCH_BUTTON).click(force=True)
            self.page.wait_for_url("**/products?search=**", timeout=4000)
        except Exception:
            self.navigate(f"https://automationexercise.com/products?search={product_name}")
        self.page.wait_for_timeout(1000)

    def is_search_results_visible(self):
        """Check if 'SEARCHED PRODUCTS' header appears."""
        try:
            self.page.locator(self.SEARCH_HEADER).first.wait_for(state="visible", timeout=5000)
            text = self.page.locator(self.SEARCH_HEADER).first.inner_text().strip()
            return "searched" in text.lower()
        except Exception:
            return False

    def get_search_results_count(self):
        """Return the number of product cards found on page."""
        self.page.wait_for_timeout(500)
        return self.page.locator(self.PRODUCT_CARDS).count()

    def click_first_product_details(self):
        """Click 'View Product' link on the first product card."""
        self.page.locator("a[href^='/product_details/']").first.click()

    def is_product_detail_displayed(self):
        """Check if the product information section (title, price, availability) is loaded."""
        return self.is_visible(".product-information", timeout=5000)

    def is_all_products_header_visible(self):
        """Verify that 'ALL PRODUCTS' header is visible."""
        return self.is_visible(self.ALL_PRODUCTS_HEADER)

    # ==========================================
    # ADD TO CART
    # ==========================================

    def add_first_product_to_cart(self):
        """Add the first product card in the catalog to the cart."""
        card = self.page.locator(self.PRODUCT_CARDS).first
        card.scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)
        product_name = card.locator(".productinfo p").inner_text().strip()
        try:
            with self.page.expect_response("**/add_to_cart/**", timeout=4000):
                card.locator(".productinfo a.add-to-cart").first.dispatch_event("click")
        except Exception:
            card.locator(".productinfo a.add-to-cart").first.dispatch_event("click")
            self.page.wait_for_timeout(1000)
        self.page.wait_for_timeout(500)
        return product_name

    def add_second_product_to_cart(self):
        """Add the second product card in the catalog to the cart."""
        try:
            btn = self.page.locator("button.close-modal")
            if btn.is_visible():
                btn.click()
                self.page.locator("#cartModal").wait_for(state="hidden", timeout=3000)
                self.page.wait_for_timeout(500)
        except Exception:
            pass

        card = self.page.locator(self.PRODUCT_CARDS).nth(1)
        card.scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)
        product_name = card.locator(".productinfo p").inner_text().strip()
        try:
            with self.page.expect_response("**/add_to_cart/**", timeout=4000):
                card.locator(".productinfo a.add-to-cart").first.dispatch_event("click")
        except Exception:
            card.locator(".productinfo a.add-to-cart").first.dispatch_event("click")
            self.page.wait_for_timeout(1000)
        self.page.wait_for_timeout(500)
        return product_name

    def click_view_cart_in_modal(self):
        """Navigate to cart page after adding an item."""
        self.navigate("https://automationexercise.com/view_cart")

    # ==========================================
    # CATEGORIES & SUBCATEGORIES
    # ==========================================

    def expand_category(self, category_name="Women"):
        """Expand a specific category accordion panel in the sidebar."""
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
        """Check if subcategories under the category panel are expanded."""
        try:
            container = self.page.locator(f"#{category_name}")
            cls = container.get_attribute("class") or ""
            if "in" in cls or "collapsing" in cls:
                return True
            return container.locator("a").first.is_visible()
        except Exception:
            return False

    def select_subcategory_by_name(self, category_name, subcategory_name):
        """Expand category and navigate to a specific subcategory."""
        self.expand_category(category_name)
        link = self.page.locator(f"#{category_name} a").filter(has_text=re.compile(subcategory_name, re.IGNORECASE)).first
        link.wait_for(state="attached", timeout=5000)
        href = link.get_attribute("href")
        if href and href.startswith("/"):
            self.navigate(f"https://automationexercise.com{href}")
        else:
            link.click(force=True)

    # ==========================================
    # 3-LEVEL HIERARCHICAL RANDOMIZATION
    # ==========================================

    def select_random_category(self):
        """Level 1: Discovers top-level categories dynamically, selects one randomly, and clicks it."""
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
        """Level 2: Discovers subcategories under the chosen category and navigates to one randomly."""
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
        """Level 3: Discovers products on the page, selects one randomly, adds it to cart, and returns its name."""
        self.page.locator(self.PRODUCT_CARDS).first.wait_for(state="visible", timeout=5000)
        cards = self.page.locator(self.PRODUCT_CARDS)
        count = cards.count()

        random_index = random.randint(0, max(0, count - 1))
        selected_card = cards.nth(random_index)
        selected_card.scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)

        selected_product_name = selected_card.locator(".productinfo p").inner_text().strip()
        try:
            with self.page.expect_response("**/add_to_cart/**", timeout=4000):
                selected_card.locator(".productinfo a.add-to-cart").first.dispatch_event("click")
        except Exception:
            selected_card.locator(".productinfo a.add-to-cart").first.dispatch_event("click")
            self.page.wait_for_timeout(1000)
        self.page.wait_for_timeout(500)

        return selected_product_name
