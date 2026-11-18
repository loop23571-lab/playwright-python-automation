from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_full_e2e_checkout_pom(page: Page):
    # Initialize page objects
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    # Execute flow across page classes
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_item_to_cart_and_checkout()

    checkout_page.fill_shipping_info("John", "Doe", "500001")
    checkout_page.complete_order()

    # Final Assertion
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()