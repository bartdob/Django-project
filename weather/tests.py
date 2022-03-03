from django.test import TestCase


class URLTest(TestCase):
    def test_testHomePage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
