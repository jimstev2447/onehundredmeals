from django.test import TestCase
from django.test import Client


class ViewsTestCase(TestCase):

    def testHello(self):
        c = Client()
        r = c.get('/hello')
        self.assertIn('Screw you, world!', r.content)

