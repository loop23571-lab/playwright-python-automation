from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_valid_login_with_pom(page: Page):
    # 1. Initialize the Login Page object
    login_page = LoginPage(page)

    # 2. Use page methods
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 3. Assertions stay in the test file
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products")).to_be_visible()