from django.test import TestCase
from covid.models import Data


class DataTest(TestCase):
    def test_setUp(self):
        Data.critical = 100
        assert Data.critical == 100
        Data.deaths = 100
        assert Data.deaths == 100
        Data.today_new_deaths = 100
        assert Data.today_new_deaths == 100
        Data.today_new_confirmed = 100
        assert Data.today_new_confirmed == 100
        Data.confirmed = 100
        assert Data.confirmed == 100
        Data.recovered = 100
        assert Data.recovered == 100






