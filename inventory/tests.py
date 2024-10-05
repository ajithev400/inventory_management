from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Item

class ItemTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_create_item(self):
        data = {'name': 'Item1', 'description': 'Test description'}
        response = self.client.post('/items/', data)
        self.assertEqual(response.status_code, 201)

    def test_read_item(self):
        item = Item.objects.create(name='Item1', description='Test description')
        response = self.client.get(f'/items/{item.id}/')
        self.assertEqual(response.status_code, 200)

    # Additional tests for update, delete, etc.
