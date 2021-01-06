import pytest
import conftest

# ------------------------------------------------ Tests
@pytest.mark.django_db
def test_signup_success(signup):
    assert signup.status_code == 201


@pytest.mark.django_db
def test_login_success(login):
    assert login.status_code == 200

