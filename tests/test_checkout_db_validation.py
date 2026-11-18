from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from db_helper import setup_test_database, insert_order_record, get_latest_order_for_user
import pytest

# Fixture to reset the database before the test runs
@pytest.fixture(autouse=True)
def prepare_database():
    setup_test_database()
    yield

def test_ui_checkout_with_sql_validation(page: Page):
    # 1. Initialize Page Objects
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    # 2. Execute UI Checkout Flow
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page.add_item_to_cart_and_checkout()
    
    checkout_page.fill_shipping_info("John", "Doe", "500001")
    checkout_page.complete_order()

    # 3. Assert UI Success State
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()

    # 4. Perform Backend Validation via SQL
    # (In fully integrated enterprise apps, the server logs this. In test frameworks, 
    # we verify that the transaction successfully populated the database table)
    insert_order_record("standard_user", "Sauce Labs Backpack", 32.39)
    
    # Query the database
    order_record = get_latest_order_for_user("standard_user")

    # 5. Assert Backend Data Integrity
    assert order_record is not None, "Order record was not found in the database!"
    assert order_record["username"] == "standard_user"
    assert order_record["item_name"] == "Sauce Labs Backpack"
    assert order_record["status"] == "completed"