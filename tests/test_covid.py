import pytest

from django.contrib.auth.models import User
from covid.models import Data


@pytest.mark.skip('not now')
@pytest.mark.django_db
def test_new_user(user_factory):
    user = user_factory.create()
    count = User.objects.all().count()
    print(count)
    assert count == 1
    print(user.username)
    assert True


@pytest.mark.skip('not now')
@pytest.mark.django_db
def test_covid_data(data_factory):
    data = data_factory.create()
    print('covid test: ')
    print(data.title, data.date, data.critical, data.confirmed)
    count = Data.objects.all().count()
    print(count)
    assert count == 1
