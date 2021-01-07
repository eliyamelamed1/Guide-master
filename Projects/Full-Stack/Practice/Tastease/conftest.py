import pytest
from rest_framework.test import APIClient
from recipes.models import Recipe

# ---------------------------------------- Set Up
@pytest.fixture
def api_client():
   return APIClient()

# ---------------------------------------- Authentication
@pytest.fixture
def signup(api_client):
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
def login(api_client, signup):
    login_url = "/users/login/"
    data = {
        "email": "testuser@gmail.com", 
        "password": "56156asd"
    }
    user_logged_in = api_client.post(login_url, data)

    return user_logged_in

@pytest.fixture
def logout(api_client):
    logout_url = "/users/logout/"
    logout = api_client.post(logout_url)

    return logout

# ---------------------------------------- Recipes
@pytest.fixture
def create_recipe(api_client):
    recipe_creation_url = '/recipes/create/'
    user_id = 1
    data = {
        'author': {user_id},
        'title': 'recipe title',
        'description': 'recipe description',
        'flavor_type': 'Sour', 
    }
    create_recipe = api_client.post(recipe_creation_url, data)

    return create_recipe


@pytest.fixture
def search_recipe(api_client):
    search_recipe_url = '/recipes/search/'
    data = {
        'flavor_type': 'Sour',
        'description': 'description',
    }

    search_recipe = api_client.post(search_recipe_url, data)

    return search_recipe

@pytest.fixture
def detail_recipe(api_client):
    recipe_id = Recipe.objects.all()[0].id
    detail_recipe_url = '/recipes/{recipe_id}/'
    detail_recipe = api_client.get(detail_recipe_url)

    return detail_recipe

# @pytest.fixture
# def update_recipe(api_client):
#     recipe_id = Recipe.objects.all()[0].id
#     data = {
#         'title': 'new recipe title'
#     }
#     detail_recipe_url = '/recipes/{recipe_id}/'
#     detail_recipe_update_info = api_client.put(detail_recipe_url, data)

#     return detail_recipe_update_info
