import pytest

from django.contrib.auth.models import User

@pytest.mark.filterwarnings
@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test', 'test@test.pl', 'test')
    User.objects.create_user('test1', 'test1@test.pl', 'test1')
    assert User.objects.count() == 2
