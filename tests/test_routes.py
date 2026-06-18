import unittest
import json
from service import app
from service.models import AccountService

class TestAccountRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        AccountService._accounts = []
        AccountService._next_id = 1

    def test_create_account(self):
        response = self.client.post('/accounts', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['name'], 'John Doe')

    def test_list_accounts(self):
        self.client.post('/accounts', json={'name': 'John', 'email': 'john@test.com', 'phone': '123'})
        response = self.client.get('/accounts')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(len(data) >= 1)

    def test_read_account(self):
        self.client.post('/accounts', json={'name': 'Jane', 'email': 'jane@test.com', 'phone': '456'})
        response = self.client.get('/accounts/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Jane')

    def test_update_account(self):
        self.client.post('/accounts', json={'name': 'Bob', 'email': 'bob@test.com', 'phone': '789'})
        response = self.client.put('/accounts/1', json={'name': 'Robert'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Robert')

    def test_delete_account(self):
        self.client.post('/accounts', json={'name': 'Alice', 'email': 'alice@test.com', 'phone': '111'})
        response = self.client.delete('/accounts/1')
        self.assertEqual(response.status_code, 204)
