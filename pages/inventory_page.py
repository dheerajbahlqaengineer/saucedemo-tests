from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_list = page.locator(".inventory_item")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def get_product_count(self):
        # Wait for products to load
        self.product_list.first.wait_for(state='visible')
        return self.product_list.count()

    def add_product_to_cart_by_index(self, index: int):
        # Wait for the specific product to be visible
        self.product_list.nth(index).wait_for(state='visible')
        # Use a more specific button locator
        add_to_cart_button = self.product_list.nth(index).locator("button:has-text('Add to cart')")
        add_to_cart_button.click()

    def get_cart_badge_count(self):
        # Wait for cart badge with multiple fallback strategies
        try:
            # Wait for badge to be visible
            self.cart_badge.wait_for(state='visible', timeout=5000)
            return int(self.cart_badge.text_content())
        except:
            # If badge not visible, check if cart is empty
            if self.cart_badge.is_hidden():
                return 0
            else:
                raise
