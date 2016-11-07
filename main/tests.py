from django.core.urlresolvers import resolve
from django.test import TestCase
from main.views import home

# Create your tests here.
class HomepageTest(TestCase):

    def test_root_resolves_to_home(self):
        root=resolve('/')
        self.assertEqual(root.func,home)