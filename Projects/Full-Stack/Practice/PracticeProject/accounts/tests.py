import pytest
import conftest

# ------------------------------------------------ Tests
@pytest.mark.django_db
def test_signup(create_user):
    assert create_user.status_code == 201


@pytest.mark.django_db
def test_login_with_email(login_user):
    assert login_user.status_code == 200

