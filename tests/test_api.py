from playwright.sync_api import APIRequestContext, expect

def test_get_user_api(playwright):
    # 1. Create an API request context (like opening a collection in Postman)
    api_context: APIRequestContext = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    # 2. Send a GET request to the /users/1 endpoint
    response = api_context.get("/users/1")

    # 3. Assert status code 200 OK (Just like in Postman tests!)
    assert response.ok
    assert response.status == 200

    # 4. Parse JSON response and validate fields
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert "email" in data
    
    # Clean up context
    api_context.dispose()