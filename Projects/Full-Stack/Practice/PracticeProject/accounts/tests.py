import pytest
import conftest

# ------------------------------------------------ Tests
@pytest.mark.django_db
def test_signup_success(create_user):
    assert create_user.status_code == 201


@pytest.mark.django_db
def test_login_success(login_user):
    assert login_user.status_code == 200

