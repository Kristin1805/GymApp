from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from GymApp.profiles.models import USER_MODEL, Profile


class CreateUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = USER_MODEL
        fields = ("username", "email")



class CustomUserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = USER_MODEL
        fields = ("username", "first_name", "last_name")

class BaseUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)


class ProfileEditForm(BaseUserForm):
    pass
