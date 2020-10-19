from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import testcases
from django.urls import reverse
from .models import Post

class BlogTest(TestCase):

    def setUser(self):
        self.user = get_user_model().objects.create_user(
            username='sizan',
            email='sizan@gmail.com',
            password="123",
        )

        self.post =Post.objects.create(
            title = "a title",
            body ="this body",
            author=self.user
        )
    def test_string_representation(self):
        post = Post(title='a simple title')
        self.assertEqual(str(post),post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(),'/post/1/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','A good TItle')
        self.assertEqual(f'{self.post.author}','A good author')
        self.assertEqual(f'{self.post.body}','A good body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'a good body')
        self.assertTemplateUsed(response,'home.html')

    def test_post_details_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,400)
        self.assertContains(response,'A good title')
        self.assertTemplateUsed(response,'post_details.html')


    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'),{
            'title':'new title',
            'body':'new body',
            'author':self.user
        })
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'new title')
        self.assertContains(response,'new body')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit',args=1),{
            'title':'update title',
            'body':'update body',
        })
        self.assertEqual(response.status_code,302)

    def test_post_delete_view(self):
        response = self.client.post(
            reverse('post_delete',args=1)
        )
        self.assertEqual(response.status_code,302)