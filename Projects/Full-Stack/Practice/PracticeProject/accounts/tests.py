import pytest
from rest_framework.test import APIClient

# Fixtures
@pytest.fixture
def api_client():
   return APIClient()


@pytest.fixture
def create_user(api_client):
    def make_user():
        signup_url = "/auth/users/"
        data = {
            "email": "testuser@gmail.com",
            "name": "testuser", 
            "password": "56156asd", 
            "re_password": "56156asd"
        }
        user_created = api_client.post(signup_url, data)
        return user_created
    return make_user()

@pytest.fixture
def login_user(api_client, create_user):
    def log_user():
        login_url = "/auth/jwt/create/"
        data = {
            "email": "testuser@gmail.com", 
            "password": "56156asd"
        }
        user_logged_in = api_client.post(login_url, data)
        return user_logged_in
    return log_user()


# Tests
@pytest.mark.django_db
def test_signup(create_user):
    assert create_user.status_code == 201

@pytest.mark.django_db
def test_login_with_email(login_user):
    assert login_user.status_code == 200

