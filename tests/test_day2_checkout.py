""" import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("jack")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("ripper")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("500000")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"inventory-item\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
 """

from playwright.sync_api import Page, expect

APP_URL = "https://www.saucedemo.com/"

# Dictionary for user and shipping info
checkout_data = {
    "username": "standard_user",
    "password": "secret_sauce",
    "first_name": "John",
    "last_name": "Doe",
    "postal_code": "500001",
    "success_message": "Thank you for your order!"
}

def test_complete_e2e_checkout(page: Page):
    # 1. Navigate and Login
    page.goto(APP_URL)
    page.get_by_placeholder("Username").fill(checkout_data["username"])
    page.get_by_placeholder("Password").fill(checkout_data["password"])
    page.get_by_role("button", name="Login").click()

    # 2. Add item to cart and go to cart
    page.get_by_role("button", name="Add to cart").first.click()
    page.locator(".shopping_cart_link").click()

    # 3. Proceed to checkout
    page.get_by_role("button", name="Checkout").click()

    # 4. Fill shipping information using dictionary values
    page.get_by_placeholder("First Name").fill(checkout_data["first_name"])
    page.get_by_placeholder("Last Name").fill(checkout_data["last_name"])
    page.get_by_placeholder("Zip/Postal Code").fill(checkout_data["postal_code"])
    page.get_by_role("button", name="Continue").click()

    # 5. Finish order
    page.get_by_role("button", name="Finish").click()

    # 6. Assert success message (Your final test validation!)
    expect(page.get_by_text(checkout_data["success_message"])).to_be_visible()