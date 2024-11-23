from unicodedata import category

from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class TestPostCanBeCreated(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='Test Category')
        test_user1 = User.objects.create_user(username='test_user1', password='<PASSWORD>')
        test_post = Post.objects.create(category_id=1,title='Test Post Title',author_id=1,
                                        content='Test Post Content',slug='test_slug',
                                        status='published',excerpt='Test Post Excerpt')


    def test_post_can_be_created(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author,'test_user1')
        self.assertEqual(excerpt,'Test Post Excerpt')
        self.assertEqual(title,'Test Post Title')
        self.assertEqual(content,'Test Post Content')
        self.assertEqual(status,'published')
        self.assertEqual(str(post),'Test Post Title')
        self.assertEqual(str(cat),'Test Category')




