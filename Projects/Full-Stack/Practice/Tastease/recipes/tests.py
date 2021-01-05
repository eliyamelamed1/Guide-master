import pytest
import conftest

# ------------------------------------------------ Tests
class Test_recipe_list:
    @pytest.mark.django_db
    def test_recipe_list_page_render_for_authenticated_users(self, api_client ,login_user):
        recipes_list_url = '/recipes/'
        page_render = api_client.get(recipes_list_url)

        assert page_render.status_code == 200


    @pytest.mark.django_db
    def test_recipe_list_page_render_for_guest_users(self, api_client):
        recipes_list_url = '/recipes/'
        page_render = api_client.get(recipes_list_url)

        assert page_render.status_code == 200


class Test_create_recipe:
    @pytest.mark.django_db
    def test_create_recipe_page_render_for_authenticated_user(self, api_client, login_user):
        recipe_creation_url = '/recipes/create/'
        recipe_creation_url_render = api_client.get(recipe_creation_url)

        # 405 method not allowed - get isnt allowed only post
        assert recipe_creation_url_render.status_code == 405 


    @pytest.mark.django_db
    def test_create_recipe_page_should_not_render_for_guest_user(self, api_client):
        recipe_creation_url = '/recipes/create/'
        recipe_creation_url_render = api_client.get(recipe_creation_url)

        assert recipe_creation_url_render.status_code == 401


    @pytest.mark.django_db
    def test_create_recipe_as_authenticated_user(self, api_client, login_user, create_recipe):
        
        assert create_recipe.status_code == 201


    @pytest.mark.django_db
    def test_create_recipe_not_allowed_for_guest_user(self, api_client, create_recipe):
        
        assert create_recipe.status_code == 401

class Test_search_recipe:
    @pytest.mark.django_db
    def test_recipe_search_render_for_authenticated_user(self, api_client, login_user):
        recipe_search_url = '/recipe/search/'
        page_render = api_client.get(recipe_search_url)

        assert page_render.status_code == 200

    @pytest.mark.django_db
    def test_recipe_search_render_for_guest_user(self, api_client):
        recipe_search_url = '/recipe/search/'
        page_render = api_client.get(recipe_search_url)

        assert page_render.status_code == 200