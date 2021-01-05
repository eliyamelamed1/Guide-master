import pytest
import conftest

# ------------------------------------------------ Tests
@pytest.mark.django_db
def test_recipes_list_page_doesnt_render_for_guest_users(api_client):
    recipes_list_url = '/recipes/'
    page_render = api_client.get(recipes_list_url)

    assert page_render.status_code == 401


@pytest.mark.django_db
def test_recipes_list_page_render_for_authenticated_users(api_client ,login_user):
    recipes_list_url = '/recipes/'
    page_render = api_client.get(recipes_list_url)

    assert page_render.status_code == 200


@pytest.mark.django_db
def test_create_recipe_page_doesnt_render_for_guest_user(api_client):
    recipe_creation_url = '/recipes/create/'
    recipe_creation_url_render = api_client.get(recipe_creation_url)

    assert recipe_creation_url_render.status_code == 401



@pytest.mark.django_db
def test_create_recipe_page_render_for_authenticated_user(api_client, login_user):
    recipe_creation_url = '/recipes/create/'
    recipe_creation_url_render = api_client.get(recipe_creation_url)

    # 405 method not allowed - get isnt allowed only post
    assert recipe_creation_url_render.status_code == 405 


@pytest.mark.django_db
def test_create_recipe_as_authenticated_user(api_client, login_user, create_recipe):
    
    assert create_recipe.status_code == 201

@pytest.mark.django_db
def test_create_recipe_as_guest_user(api_client, create_recipe):
    
    assert create_recipe.status_code == 401

