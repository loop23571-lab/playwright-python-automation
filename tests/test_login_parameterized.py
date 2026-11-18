import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

# 1. Define your test datasets using the decorator
@pytest.mark.parametrize(
    "username, password, expected_outcome",
    [
        ("standard_user", "secret_sauce", "success"),
        ("locked_out_user", "secret_sauce", "error"),
        ("performance_glitch_user", "secret_sauce", "success"),
        ("invalid_user", "wrong_password", "error"),
    ]
)
def test_login_data_driven(page: Page, username, password, expected_outcome):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    # 2. Assertions based on expected outcome
    if expected_outcome == "success":
        # Verify user reached the inventory page
        expect(page.locator(".inventory_container")).to_be_visible()
    else:
        # Verify error message is displayed for invalid logins
        expect(page.locator("[data-test='error']")).to_be_visible()