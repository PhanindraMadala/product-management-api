import unittest
from service.routes import app

class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    # READ test case
    def test_read_product(self):
        response = self.client.get('/products/1')
        self.assertEqual(response.status_code, 200)

    # UPDATE test case
    def test_update_product(self):
        response = self.client.put('/products/1', json={"name": "Updated Product"})
        self.assertEqual(response.status_code, 200)

    # DELETE test case
    def test_delete_product(self):
        response = self.client.delete('/products/1')
        self.assertEqual(response.status_code, 204)

    # LIST ALL test case
    def test_list_all_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)

    # LIST BY NAME test case
    def test_list_by_name(self):
        response = self.client.get('/products?name=Laptop')
        self.assertEqual(response.status_code, 200)

    # LIST BY CATEGORY test case
    def test_list_by_category(self):
        response = self.client.get('/products?category=Electronics')
        self.assertEqual(response.status_code, 200)

    # LIST BY AVAILABILITY test case
    def test_list_by_availability(self):
        response = self.client.get('/products?availability=True')
        self.assertEqual(response.status_code, 200)
 
