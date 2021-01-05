import pytest
import conftest

# ------------------------------------------------ Tests
@pytest.mark.django_db
def test_recipes_list_page_doesnt_render_for_guest_users(api_client):
    recipes_list_url = '/recipes/'
    page_render = api_client.get(recipes_list_url)

    assert page_render.status_code == 401


@pytest.mark.django_db
def test_recipes_list_page_render_for_authenticated_users(api_client,login_user):
    recipes_list_url = '/recipes/'
    page_render = api_client.get(recipes_list_url)

    assert page_render.status_code == 200


