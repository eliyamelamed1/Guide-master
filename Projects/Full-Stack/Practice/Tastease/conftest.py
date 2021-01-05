import pytest
from rest_framework.test import APIClient

# ---------------------------------------- Set Up
@pytest.fixture
def api_client():
   return APIClient()

# ---------------------------------------- Authentication
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

    return user_created


@pytest.fixture
def login_user(api_client, create_user):
    login_url = "/users/login/"
    data = {
        "email": "testuser@gmail.com", 
        "password": "56156asd"
    }
    user_logged_in = api_client.post(login_url, data)

    return user_logged_in


# ---------------------------------------- Recipes
@pytest.fixture
def create_recipe(api_client):
    recipe_creation_url = '/recipes/create/'
    user_id = 1

    data = {
        'author': {user_id},
        'title': 'recipe title',
        'description': 'recipe description',
        'method_type': 'Cook', 
        'flavor_type': 'Sour', 
        'difficulty_type': 'Easy',
    }
    create_recipe = api_client.post(recipe_creation_url, data)

    return create_recipe