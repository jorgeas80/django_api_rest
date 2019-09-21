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
        # name and slug fields are required
        prod_serializer = ProductSerializer(data=self.data)
        self.assertFalse(prod_serializer.is_valid())
        self.assertIn('name', prod_serializer.errors)
        self.assertIn('slug', prod_serializer.errors)

    def test_product_serialization_correct(self):
        # Update data with required fields
        name = 'Two Scoops of Django'
        self.data.update({
            'name': name,
            'slug': slugify(name)
        })
        # Serialize data and check is stored at db
        prod_serializer = ProductSerializer(data=self.data)
        self.assertTrue(prod_serializer.is_valid())
        prod_serializer.save()
        self.assertEqual(Product.objects.count(), 1)

        # Check stored data
        p = Product.objects.first()
        self.assertEqual(p.name, self.data.get('name'))
        self.assertEqual(p.description, self.data.get('description'))
        self.assertEqual(p.price, self.data.get('price'))
        self.assertEqual(p.slug, self.data.get('slug'))

    def test_product_partial_serialization_correct(self):
        # Update and serialize data again
        name = 'Two Scoops of Django'
        self.data.update({
            'name': name,
            'slug': slugify(name)
        })
        prod_serializer = ProductSerializer(data=self.data)
        self.assertTrue(prod_serializer.is_valid())
        prod_serializer.save()
        self.assertEqual(Product.objects.count(), 1)

        p = Product.objects.first()

        # Update by partial serialization
        prod_serializer = ProductSerializer(instance=p, data={'price': 60}, partial=True)
        self.assertTrue(prod_serializer.is_valid())
        prod_serializer.save()

        # Check data is updated
        self.assertEqual(Product.objects.count(), 1)
        p.refresh_from_db()
        self.assertEqual(p.price, 60)