from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms

from GymApp.profiles.models import USER_MODEL, Profile


class CreateUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = USER_MODEL
        fields = ("username", "email")
class UserProfileForm(UserChangeForm):
    class Meta:
        model = USER_MODEL
        fields = ['username', 'email', 'first_name', 'last_name']  # Include user fields you want to edit

    gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female')), required=False)
    phone_number = forms.CharField(max_length=10, required=False)
    address = forms.CharField(max_length=255, required=False)
    image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        try:
            profile = self.instance.profile
            self.fields['gender'].initial = profile.gender
            self.fields['phone_number'].initial = profile.phone_number
            self.fields['address'].initial = profile.address
        except Profile.DoesNotExist:
            pass

    def save(self, commit=True):
        user_instance = super(UserProfileForm, self).save(commit=False)
        profile, created = Profile.objects.get_or_create(user=user_instance)

        # Save profile fields
        profile.gender = self.cleaned_data['gender']
        profile.phone_number = self.cleaned_data['phone_number']
        profile.address = self.cleaned_data['address']

        # Save user and profile
        if commit:
            user_instance.save()
            profile.save()

        return user_instance

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

class ProfileDetailsForm(BaseUserForm):
    pass