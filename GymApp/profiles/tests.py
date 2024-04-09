from django.test import TestCase, RequestFactory

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from GymApp.workouts.models import Plan
from GymApp.profiles.models import Profile, PlanWorkout
from .views import UserRegistrationView, UserLoginView, update_profile
from ..workouts_in_plan.models import Workout


class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        # Check if a profile already exists for the user and delete it
        if hasattr(self.user, 'profile'):
            self.user.profile.delete()

    def test_profile_creation(self):
        profile = Profile.objects.create(
            user=self.user,
            gender='M',
            phone_number='1234567890',
            address='Test Address',
            is_trainer=True,
            card_num=123
        )
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.gender, 'M')

class UserRegistrationViewTestCase(TestCase):
    def test_registration_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    # Add more tests for form submission and validation if needed

class UserLoginViewTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_login_view(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')

    # Add more tests for login functionality


# Add more tests as necessary for each model and view

class UpdateProfileViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        # Check if a profile already exists for the user before creating a new one
        if not hasattr(self.user, 'profile'):
            self.profile = Profile.objects.create(
                user=self.user,
                gender='M',
                phone_number='1234567890',
                address='Test Address',
                is_trainer=True,
                card_num=1234567890123456
            )

    def test_update_profile_view_get(self):
        request = self.factory.get(reverse('profile_edit'))
        request.user = self.user
        response = update_profile(request)
        self.assertEqual(response.status_code, 200)

