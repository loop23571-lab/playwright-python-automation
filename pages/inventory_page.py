from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart").first
        self.cart_icon = page.locator(".shopping_cart_link")
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def add_item_to_cart_and_checkout(self):
        self.add_to_cart_button.click()
        self.cart_icon.click()
        self.checkout_button.click()