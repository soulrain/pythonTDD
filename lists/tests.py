from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #1
        response = home_page(request) #2
        self.assertTrue(response.content.startswith('<html>')) #3
        self.assertIn('<title>To-Do lists</title>', response.content) #4
        self.assertTrue(response.content.endswith('</html>')) #5
