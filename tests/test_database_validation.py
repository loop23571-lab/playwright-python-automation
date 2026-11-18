from db_helper import setup_test_database, query_user_status
import pytest

# Pytest fixture to set up the database before tests run
@pytest.fixture(autouse=True)
def prepare_db():
    setup_test_database()
    yield

def test_user_status_in_database():
    # 1. Query the database using your SQL logic
    status = query_user_status("standard_user")

    # 2. Assert the backend database state matches expected QA criteria
    assert status == "active", f"Expected user status to be active, but got {status}"