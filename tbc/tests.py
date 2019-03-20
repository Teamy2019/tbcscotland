from django.contrib.staticfiles import finders
from django.test import TestCase
from tbc.models import Profile, LendAndSell
from tbc.forms import CommentsForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your tests here.

class ViewsCountTest(TestCase):

    def test_views_count(self):
        user = User.objects.get_or_create(username="testuser", password="test1234", email="testuser@testuser.com")[0]
        user.set_password(user.password)
        user.save()

        user_profile = Profile.objects.get_or_create(user=user, username="testuser", views=-1)[0]
        user_profile.save()

        self.assertFalse((user_profile.views >= 0), True)


class AnotherTest(TestCase):

    def test_another_test(self):
        response = self.client.get(reverse('post_project'))
        # should equal 302 as this would be a redirect to login page
        self.assertEqual(response.status_code, 302)


class ProfileTest(TestCase):

    def test_username(self):
        user = User.objects.get_or_create(username="testuser", password="test1234", email="testuser@testuser.com")[0]
        user.set_password(user.password)
        user.save()

        user_profile = Profile.objects.get_or_create(user=user, username="testuser")[0]
        user_profile.save()

        self.assertTrue((user_profile.username == 'testuser'))


class ServeStaticFiles(TestCase):

    def test_serving_static_files(self):

        result = finders.find('icons/update.png')
        self.assertIsNotNone(result)


class SlugLineCreation(TestCase):

    def test_slug_line_creation(self):
        """
        slug_line_creation checks to make sure that when we add a category an appropriate slug line is created
        i.e. "Random Category String" -> "random-category-string"
        """
        user = User.objects.get_or_create(username="testuser", password="test1234", email="testuser@testuser.com")[0]
        user.set_password(user.password)
        user.save()

        user_profile = Profile.objects.get_or_create(user=user, username="testuser")[0]
        user_profile.save()

        las = LendAndSell(profile=user_profile, title='Guitar For Sale')
        las.save()
        self.assertEqual(las.slug, 'guitar-for-sale')


class FormTest(TestCase):

    def test_with_blank(self):
        form = CommentsForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'comment': ['This field is required.'],
        })
