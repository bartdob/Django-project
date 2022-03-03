import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def user_1(db):
    user = User.objects.create_user('test', 't@t.pl', 'test-pass')
    return user


def test_set_check_password(user_1):
    assert user_1.username == "test"
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True
