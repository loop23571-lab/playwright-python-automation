from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.postal_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.finish_button = page.get_by_role("button", name="Finish")

    def fill_shipping_info(self, first: str, last: str, zip_code: str):
        self.first_name_input.fill(first)
        self.last_name_input.fill(last)
        self.postal_code_input.fill(zip_code)
        self.continue_button.click()

    def complete_order(self):
        self.finish_button.click()