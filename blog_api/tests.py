from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User


class PostTestCases(APITestCase):

      def test_view_post(self):
            url = reverse('blog_api:listcreate') #takes the endpoint
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

      def test_create_post(self):
            self.test_category = Category.objects.create(name='Test Category')
            self.test_user1 = User.objects.create_user(username='test_user1', password='<PASSWORD>')
            data = {'title': 'test_title','author': 1, 'excerpt': 'test_excerpt', 'content': 'test_content'}
            url = reverse('blog_api:listcreate') #takes the endpoint
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)





