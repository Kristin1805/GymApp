from django.test import TestCase
from django.contrib.auth import get_user_model

from GymApp.profiles.forms import CreateUser, UserProfileForm, CustomUserEditForm, ProfileDetailsForm

USER_MODEL = get_user_model()

class CreateUserFormTestCase(TestCase):
    def test_create_user_form_valid(self):
        form_data = {'username': 'testuser', 'email': 'test@example.com', 'password1': 'ILoveCats123', 'password2': 'ILoveCats123'}
        form = CreateUser(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_user_form_invalid(self):
        form_data = {'username': '', 'email': 'test@example.com'}  # Empty username and pass
        form = CreateUser(data=form_data)
        self.assertFalse(form.is_valid())






