import unittest
from app import create_app

class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_consume(self):
        response = self.client.get('/consume')
        self.assertEqual(response.status_code, 200)
        self.assertIn('full_name', response.get_json())

    def test_quote(self):
        response = self.client.get('/quote')
        self.assertEqual(response.status_code, 200)
        self.assertIn('content', response.get_json())
        self.assertIn('author', response.get_json())

if __name__ == '__main__':
    unittest.main()
