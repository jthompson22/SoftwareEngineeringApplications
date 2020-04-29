from django.test import TestCase
from django.test import Client
from .views import water_quantity
from .rivernet_api import Get_Site_Information

class pollsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def testBasicPost():
        response = c.get('')
        print(response)
        self.assertEqual(response.status_code, 200)

    def testJSONRequest():
        site_dictionary = Get_Site_Information()
        self.assertTrue(site_dictionary != None)
