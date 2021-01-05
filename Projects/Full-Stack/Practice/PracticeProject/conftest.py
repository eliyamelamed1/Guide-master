import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

# ------------------------------------------------Fixtures
@pytest.fixture
def api_client():
   return APIClient()


@pytest.fixture
def create_user(api_client):
    signup_url = "/auth/users/"
    data = {
        "email": "testuser@gmail.com",
        "name": "testuser", 
        "password": "56156asd", 
        "re_password": "56156asd"
    }
    user_created = api_client.post(signup_url, data)

    assert user_created.status_code == 201
    return user_created

@pytest.fixture
def login_user(api_client, create_user):
    login_url = "/users/login/"
    data = {
        "email": "testuser@gmail.com", 
        "password": "56156asd"
    }
    user_logged_in = api_client.post(login_url, data)

    assert user_logged_in.status_code == 200
    return user_logged_in