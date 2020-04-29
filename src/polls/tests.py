from django.test import TestCase
from django.test import Client
from .views import water_quantity

class pollsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def testBasicPost():
        response = c.get('')
        print(response)
        self.assertEqual(response.status_code, 200)
