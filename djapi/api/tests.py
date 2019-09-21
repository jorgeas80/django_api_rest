from django.test import TestCase


# Create your tests here.
class ApiSerializerTestCase(TestCase):
    fixtures = ['api/fixtures/categories.json', 'api/fixtures/subcategories.json']

    @classmethod
    def setUpTestData(cls):
        cls.data = {
            "subcategory": 1,
            "description": "Desarrollo Web con Python usando Django 2.1",
            "date_created": "2019-09-01T12:11:37.090335Z"
        }

    def test_foo(self):
        self.assertTrue(True)
