from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission # new
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

# change Profile as: the author of the Profile / logged in user / logged out user
# access Profile list view while: logged in / logged out
class ProfileTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', 
            password='abc123',
        )
        testuser1.save()

        # Create a blog Profile
        test_profile = Profile.objects.create(
            # author=testuser1, 
            first_name='Blog first_name', 
            about_me='about_me content...'
        )
        test_profile.save()

    def test_blog_content(self):
        profile = Profile.objects.get(id=1)
        # author = f'{Profile.author}'
        first_name = f'{profile.first_name}'
        about_me = f'{profile.about_me}'
        # self.assertEqual(author, 'testuser1')
        self.assertEqual(first_name, 'Blog first_name')
        self.assertEqual(about_me, 'about_me content...')

    # def test_book_list_view_for_logged_in_user(self):
    #     self.client.login(username='testuser1', password='abc123')









# TODO 
# TEST for Profile view while log in and while log out