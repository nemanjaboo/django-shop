from django.contrib.auth.models import User
from django.test import TestCase

from bookstore.models import Books, Category

# for the testing, i am using COVERAGE ( pip install coverage)
# coverage HTML - creates HTML for testing report
# coverage report - runs a report on needed tests, open index.html for more
# coverage run --omit='*/venv/*' manage.py test --- > command to exclude virtual env folder from testing 


class TestCategoriesModel(TestCase):
    # tests should always be named to be easy for understanding
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')
        # set up is stage in testing where we create data to test against
    def test_category_model_entry(self):
        """
        Test of Category model data insertion/type/fields attributes
        """

        data = self.data1
        self.assertTrue(isinstance(data, Category))


    def test_category_model_entry(self):
        """
        Test of Category model name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')

class TestBooksModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin') # we need a User to create a product
        self.data1 = Books.objects.create(category_id=1, title='django beginners', # cateogry_id is the default ID models get when created
        created_by_id=1, slug='django-beginners', price='20.00', image='django') 

    def test_books_model_entry(self):
        """
        Test of Books model data insertion/types/fields attributes
        """

        data = self.data1
        self.assertTrue(isinstance(data, Books))
        self.assertEqual(str(data), 'django beginners')