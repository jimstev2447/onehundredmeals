from django.test import TestCase
from django.test import Client

class ViewsTestClass(TestCase):
    def testhello(self):
        """Verifies text in response"""
        testclient = Client()
        response = testclient.get('/hello')
        self.assertIn('Screw you, world!', str(response.content))
