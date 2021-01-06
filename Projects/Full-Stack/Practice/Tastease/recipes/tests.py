import pytest
import conftest
from .models import Recipe

# ------------------------------------------------ Tests
class Test_recipe_list:
    class Test_authenticated_users:
        @pytest.mark.django_db
        def test_recipe_list_page_render_for_authenticated_users(self, api_client ,login):
            recipes_list_url = '/recipes/'
            page_render = api_client.get(recipes_list_url)

            assert page_render.status_code == 200

    class Test_guest_users:
        @pytest.mark.django_db
        def test_recipe_list_page_render_for_guest_users(self, api_client):
            recipes_list_url = '/recipes/'
            page_render = api_client.get(recipes_list_url)

            assert page_render.status_code == 200


class Test_create_recipe:
    class Test_authenticated_users:
        @pytest.mark.django_db
        def test_create_recipe_page_render_for_authenticated_user(self, api_client, login):
            recipe_creation_url = '/recipes/create/'
            recipe_creation_url_render = api_client.get(recipe_creation_url)

            # 405 method not allowed - get isnt allowed only post
            assert recipe_creation_url_render.status_code == 405

        @pytest.mark.django_db
        def test_create_recipe_as_authenticated_user(self, api_client, login, create_recipe):
            recipe_title = Recipe.objects.all()[0].title
            recipe_description = Recipe.objects.all()[0].description
            flavor_type = Recipe.objects.all()[0].flavor_type

            
            assert recipe_title == 'recipe title'
            assert recipe_description == 'recipe description'
            assert flavor_type == 'Sour'
            assert create_recipe.status_code == 201

    class Test_guest_users:
        @pytest.mark.django_db
        def test_create_recipe_page_should_not_render_for_guest_user(self, api_client):
            recipe_creation_url = '/recipes/create/'
            recipe_creation_url_render = api_client.get(recipe_creation_url)

            assert recipe_creation_url_render.status_code == 405

        @pytest.mark.django_db
        def test_create_recipe_not_allowed_for_guest_user(self, api_client, create_recipe):
            
            assert create_recipe.status_code == 401


class Test_search_recipe:
    class Test_authenticated_users:
        @pytest.mark.django_db
        def test_recipe_search_page_render_for_authenticated_user(self, api_client, login):
            recipe_search_url = '/recipes/search/'
            page_render = api_client.get(recipe_search_url)

            assert page_render.status_code == 405 # 405 method not allowed - get isnt allowed only post

        @pytest.mark.django_db
        def test_recipe_search_successfull_for_authenticated_users(self,api_client,login,search_recipe):
            assert search_recipe.status_code == 200

    class Test_guest_users:
        @pytest.mark.django_db
        def test_recipe_search_page_render_for_guest_user(self, api_client):
            recipe_search_url = '/recipes/search/'
            page_render = api_client.get(recipe_search_url)

            assert page_render.status_code == 405 # 405 method not allowed - get isnt allowed only post

        @pytest.mark.django_db
        def test_recipe_search_successfull_for_guest_users(self,api_client,search_recipe):
            assert search_recipe.status_code == 200

class Test_recipe_details:
        class Test_authenticated_users:
            @pytest.mark.django_db
            def test_recipe_detail_render_for_authenticated_users(self, api_client, login, create_recipe ,detail_recipe):

                assert detail_recipe.status_code == 200

            @pytest.mark.django_db
            def test_recipe_details_load_for_authenticated_users(self, api_client,login, create_recipe):
                recipe_title = Recipe.objects.all()[0].title
                recipe_description = Recipe.objects.all()[0].description
                flavor_type = Recipe.objects.all()[0].flavor_type

                assert recipe_title == 'recipe title'
                assert recipe_description == 'recipe description'
                assert flavor_type == 'Sour'


            # @pytest.mark.django_db
            # def test_delete_recipe_as_authenticated_user(self, api_client, login, create_recipe):
            #     recipe_id = Recipe.objects.all()[0].id

            #     delete_recipe_url = '/recipes/{recipe_id}/'
            #     delete_recipe = api_client.delete(delete_recipe_url)

            #     assert delete_recipe.status_code == 200

        class Test_guest_users:
            @pytest.mark.django_db
            def test_recipe_detail_page_render_for_guest_users(self, api_client,login, create_recipe ,logout, detail_recipe):
                recipe_title = Recipe.objects.all()[0].title

                assert recipe_title == 'recipe title'
                assert detail_recipe.status_code == 200

            @pytest.mark.django_db
            def test_recipe_details_load_for_guest_users(self, api_client,login, create_recipe,logout,detail_recipe):
                recipe_title = Recipe.objects.all()[0].title
                recipe_description = Recipe.objects.all()[0].description
                flavor_type = Recipe.objects.all()[0].flavor_type

                assert recipe_title == 'recipe title'
                assert recipe_description == 'recipe description'
                assert flavor_type == 'Sour'

