from playwright.sync_api import Page, expect
import pytest

APP_URL = "https://www.saucedemo.com/"

# 1. Create a custom Pytest fixture for logging in as standard_user
@pytest.fixture
def logged_in_page(page: Page):
    page.goto(APP_URL)
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    # Yield hands control over to the test function once login is complete
    yield page

# 2. Test 1 now focuses ONLY on what happens AFTER a successful login
def test_product_page_loads(logged_in_page: Page):
    # Notice we didn't write login code here! The fixture did it for us.
    expect(logged_in_page.get_by_text("Products")).to_be_visible()

# 3. Test 2 for locked out user doesn't need the fixture because it fails early
def test_locked_out_user(page: Page):
    page.goto(APP_URL)
    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Epic sadface: Sorry, this user has been locked out.")).to_be_visible()