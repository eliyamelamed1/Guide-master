import pytest
import conftest
from .models import Recipe

# ------------------------------------------------ Tests
class TestRecipeList:
    class TestAuthenticatedUsers:
        @pytest.mark.django_db
        def test_recipe_list_page_render_for_authenticated_users(self, api_client ,login):
            recipe_list_url = '/recipes/'
            recipe_list_page_render = api_client.get(recipe_list_url)

            assert recipe_list_page_render.status_code == 200

    class TestGuestUsers:
        @pytest.mark.django_db
        def test_recipe_list_page_render_for_guest_users(self, api_client):
            recipe_list_url = '/recipes/'
            recipe_list_page_render = api_client.get(recipe_list_url)

            assert recipe_list_page_render.status_code == 200


class TestCreateRecipe:
    class TestAuthenticatedUsers:
        @pytest.mark.django_db
        def test_create_recipe_page_render_for_authenticated_user(self, api_client, login):
            create_recipe_url = '/recipes/create/'
            create_recipe_page_render = api_client.get(create_recipe_url)

            assert create_recipe_page_render.status_code == 405 # 405 method not allowed - get isnt allowed only post

        @pytest.mark.django_db
        def test_create_recipe_as_authenticated_user(self, api_client, login, create_recipe):
            recipe_created_successflly = create_recipe
            recipe_info = Recipe.objects.all()[0]

            assert recipe_created_successflly.status_code == 201
            assert recipe_info.title == 'recipe title'
            assert recipe_info.description == 'recipe description'
            assert recipe_info.flavor_type == 'Sour'

    class TestGuestUsers:
        @pytest.mark.django_db
        def test_create_recipe_page_should_not_render_for_guest_user(self, api_client):
            create_recipe_url = '/recipes/create/'
            create_recipe_page_render_error = api_client.get(create_recipe_url)

            assert create_recipe_page_render_error.status_code == 401 # 405 method not allowed - get isnt allowed only post

        @pytest.mark.django_db
        def test_create_recipe_not_allowed_for_guest_user(self, api_client, create_recipe):
            recipe_creation_error = create_recipe
            
            assert recipe_creation_error.status_code == 401


class TestSearchRecipe:
    class TestAuthenticatedUsers:
        @pytest.mark.django_db
        def test_search_recipe_page_render_for_authenticated_user(self, api_client, login):
            search_recipe_url = '/recipes/search/'
            search_recipe_page_render = api_client.get(search_recipe_url)

            assert search_recipe_page_render.status_code == 405 # 405 method not allowed - get isnt allowed only post

        @pytest.mark.django_db
        def test_search_recipe_successfull_for_authenticated_users(self,api_client,login,search_recipe):
            recipe_searched_successfuly = search_recipe

            assert recipe_searched_successfuly.status_code == 200

    class TestGuestUsers:
        @pytest.mark.django_db
        def test_search_recipe_page_render_for_guest_user(self, api_client):
            search_recipe_url = '/recipes/search/'
            search_recipe_page_render = api_client.get(search_recipe_url)

            assert search_recipe_page_render.status_code == 405 # 405 method not allowed - get isnt allowed only post

        @pytest.mark.django_db
        def test_search_recipe_successfull_for_guest_users(self,api_client,search_recipe):
            recipe_searched_successfuly = search_recipe

            assert recipe_searched_successfuly.status_code == 200

class TestRecipeDetails:
        class TestAuthenticatedUsers:
            @pytest.mark.django_db
            def test_recipe_detail_render_for_authenticated_users(self, api_client, login, create_recipe ,detail_recipe):
                detail_recipe_page_render = detail_recipe

                assert detail_recipe_page_render.status_code == 200

            # @pytest.mark.django_db
            # def test_recipe_details_load_for_authenticated_users(self, api_client,login, create_recipe):
            # add test to get info from recipe detail page

            # @pytest.mark.django_db
            # def test_delete_recipe_as_authenticated_user(self, api_client, login, create_recipe):
            #     recipe_id = Recipe.objects.all()[0].id

            #     delete_recipe_url = '/recipes/{recipe_id}/'
            #     delete_recipe = api_client.delete(delete_recipe_url)

            #     assert delete_recipe.status_code == 200

        class TestGuestUsers:
            @pytest.mark.django_db
            def test_recipe_detail_page_render_for_guest_users(self, api_client,login, create_recipe ,logout, detail_recipe):
                detail_recipe_page_render = detail_recipe
                assert detail_recipe_page_render.status_code == 200

            # @pytest.mark.django_db
            # def test_recipe_details_load_for_authenticated_users(self, api_client,login, create_recipe):
            # add test to get info from recipe detail page
