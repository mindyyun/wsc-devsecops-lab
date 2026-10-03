def test_profile_requires_login(client):
    assert client.get("/api/users/1/profile").status_code == 401


def test_user_can_get_their_profile(client):
    client.get("/login/alice")

    response = client.get("/api/users/1/profile")

    assert response.status_code == 200
    assert response.get_json() == {
        "id": 1,
        "username": "alice",
        "full_name": "Alice Anand",
        "email": "alice@example.com",
        "phone": "555-0101",
        "home_address": "101 Maple Ave, Springfield",
    }


def test_user_cannot_get_another_users_profile(client):
    client.get("/login/alice")

    assert client.get("/api/users/2/profile").status_code == 403


def test_missing_profile_is_not_found(client):
    client.get("/login/alice")

    assert client.get("/api/users/999/profile").status_code == 404