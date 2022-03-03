import random
import factory

from django.contrib.auth.models import User
from covid import models
from faker import Faker
fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = 'True'


class DataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Data

    title = 'test'
    date = fake.date_object()
    critical = random.randint(1, 1000)
    deaths = random.randint(1, 1000)
    today_new_deaths = random.randint(1, 1000)
    today_new_confirmed = random.randint(1, 1000)
    confirmed = random.randint(1, 1000)
    recovered = random.randint(1, 1000)

