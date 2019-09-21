from django.test import TestCase
from django.utils.text import slugify
from .models import Product
from .serializers import ProductSerializer


# Create your tests here.
class ApiSerializerTestCase(TestCase):
    fixtures = ['api/fixtures/categories.json', 'api/fixtures/subcategories.json']

    def setUp(self):
        # If we define this as setUpTestData and call self.data.update, we need to
        # restore dict after each call (using tearDown)
        self.data = {
            "subcategory": 1,
            "description": "Best practices for Django",
            "price": 50,
            "create_date": "2019-09-01T12:11:37.090335Z"
        }

    def test_product_serialization_incorrect_missing_field(self):
        prod_serializer = ProductSerializer(data=self.data)
        self.assertFalse(prod_serializer.is_valid())
        self.assertIn('name', prod_serializer.errors)

    def test_product_serialization_correct(self):
        name = 'Two Scoops of Django'
        self.data.update({
            'name': name,
            'slug': slugify(name)
        })
        prod_serializer = ProductSerializer(data=self.data)
        self.assertTrue(prod_serializer.is_valid())
