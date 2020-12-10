from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission # new
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# create post while: login / logout
# change post as: the author of the post / logged in user / logged out user
# access post list view while: logged in / logged out
class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', 
            password='abc123',
        )
        testuser1.save()

        # Create a blog post
        test_post = Post.objects.create(
            # author=testuser1, 
            title='Blog title', 
            description='description content...'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        # author = f'{post.author}'
        title = f'{post.title}'
        description = f'{post.description}'
        # self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(description, 'description content...')

    # def test_book_list_view_for_logged_in_user(self):
    #     self.client.login(username='testuser1', password='abc123')









# TODO 
# TEST for post view while log in and while log out