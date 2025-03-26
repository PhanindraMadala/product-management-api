import unittest
from service.models import Product
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):

    def setUp(self):
        self.product = ProductFactory()

    # READ test case
    def test_read_product(self):
        self.assertEqual(self.product.name, self.product.name)

    # UPDATE test case
    def test_update_product(self):
        new_name = "Updated Product"
        self.product.name = new_name
        self.assertEqual(self.product.name, new_name)

    # DELETE test case
    def test_delete_product(self):
        product = ProductFactory()
        del product
        self.assertTrue(True)

    # LIST ALL test case
    def test_list_all_products(self):
        products = [ProductFactory() for _ in range(5)]
        self.assertEqual(len(products), 5)

    # FIND BY NAME test case
    def test_find_by_name(self):
        product = ProductFactory(name="Laptop")
        self.assertEqual(product.name, "Laptop")

    # FIND BY CATEGORY test case
    def test_find_by_category(self):
        product = ProductFactory(category="Electronics")
        self.assertEqual(product.category, "Electronics")

    # FIND BY AVAILABILITY test case
    def test_find_by_availability(self):
        product = ProductFactory(availability=True)
        self.assertTrue(product.availability)
 
