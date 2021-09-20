from unittest import skip

from django.contrib.auth.models import User
# unittest skip provides us an option of skipping tests
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from bookstore.models import Books, Category
from bookstore.views import all_books

# acts as a dummy Web browser 


# @skip("demonstrating skipping")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass
class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client() # we can now access our client as "c"
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Books.objects.create(category_id=1, title='django beginners', 
        created_by_id=1, slug='django-beginners', price='20.00', image='django') 

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts"""
        response = self.c.get('/') # get request for the homepage
        self.assertEqual(response.status_code, 200)

    def test_book_detail_url(self):
        """
        Test book page response status
        """
        response = self.c.get(reverse('bookstore:book_detail', args=['django-beginners'])) # slug must match slug in setup (django-beginners)
        self.assertEqual(response.status_code, 200)
    

    def test_category_detail_url(self):
        """
        Test category page response status
        """
        response = self.c.get(reverse('bookstore:category_list', args=['django'])) # slug matches slug in category create objects
        self.assertEqual(response.status_code, 200)
    

    def test_homepage_html(self):
        request = HttpRequest() # we need to import HttpRequests
        response = all_books(request)  # we are sending the Http request to the actual view we wrote ( need to import our views)
        html = response.content.decode('utf8') # getting all the HTML from the page, that we can check against
        self.assertIn('<title>nBooks</title>', html) # -- assertIn checks if something is inside
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
    

    def test_view_function(self):
        request = self.factory.get('/komo')
        response = all_books(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>nBooks</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    