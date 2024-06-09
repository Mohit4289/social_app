from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class APITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_user_signup(self):
        # Test user signup endpoint
        response = self.client.post('/api/signup/', {'email': 'newuser@example.com', 'password': 'newpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        # Test user login endpoint
        response = self.client.post('/api/login/', {'email': 'test@example.com', 'password': 'testpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_search_users_authenticated(self):
        # Test search users endpoint with authentication
        self.client.force_login(self.user)  # Authenticate user
        response = self.client.get('/api/search/?q=test', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Should return 200 when authenticated
        # Add more assertions based on the response data if needed

    def test_search_users_unauthenticated(self):
        # Test search users endpoint without authentication
        response = self.client.get('/api/search/?q=test', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Should return 401 when unauthenticated

    # Add more test methods for other endpoints...
