from django import forms
from django.contrib.auth.forms import UserCreationForm

from GymApp.profiles.models import USER_MODEL
from GymApp.trainers.models import Trainer



# Create your views here.
class BaseTrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        exclude = ("user",)

class CreateTrainer(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = USER_MODEL
        fields = ("username", "email")

class TrainerLoginForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields=('username','password')

class TraineViewForm(forms.ModelForm):
    class Meta:
        model= Trainer
        fields=('full_name','mobile','address','detail','img')

class TrainerEditForm(BaseTrainerForm):
    pass
