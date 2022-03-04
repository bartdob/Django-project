from django.contrib.admin import register
from tests.factories import UserFactory, DataFactory

register(UserFactory)
register(DataFactory)
