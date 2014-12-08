from django.test import TestCase, LiveServerTestCase, Client
# from django.utils import timezone
from .models import Post


class PostTest(TestCase):
    def test_create_post(self):
        # Create the post
        post = Post()
        # Set the attributes
        post.title = 'My first post'
        post.description = 'This is my first blog post'
        # post.published = True
        # post.created = timezone.now()
        # Save it
        post.save()
        # Check we can find it
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, post)
        # Check attributes
        self.assertEquals(only_post.title, 'My first post')
        self.assertEquals(only_post.description, 'This is my first blog post')
        # self.assertEquals(only_post.created.day, post.created.day)
        # self.assertEquals(only_post.created.month, post.created.month)
        # self.assertEquals(only_post.created.year, post.created.year)
        # self.assertEquals(only_post.created.hour, post.created.hour)
        # self.assertEquals(only_post.created.minute, post.created.minute)
        # self.assertEquals(only_post.created.second, post.created.second)


class AdminTest(LiveServerTestCase):
    def test_login(self):
        # Create client
        c = Client()

        # Get login page
        response = c.get('/admin/')

        # Check response code
        self.assertEquals(response.status_code, 200)
