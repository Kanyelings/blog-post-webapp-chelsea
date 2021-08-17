from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
class BlogTest(TestCase):
    def Setup(self):
        self.user = get_user_model().object.create_user(
            username='testuser',
            email='test@email.com',
            password='seret'
        )
        self.post = Post.object.create(
            title='A good title',
            body='Nice body',
            author='self.user',
        )

    def test_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.body}', 'Nice body')
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_list_view(self):
        response = Client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = Client.get('/post/i/')
        no_response = Client.get('post/100000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')
