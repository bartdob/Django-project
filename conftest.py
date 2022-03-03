from pytest_factoryboy import register
from tests.factories import UserFactory
from tests.factories import DataFactory

register(UserFactory)
register(DataFactory)
