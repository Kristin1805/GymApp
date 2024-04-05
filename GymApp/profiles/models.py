from django.contrib.auth import get_user_model
from django.db import models

from GymApp.people.models import Member

# Create your models here.
USER_MODEL = get_user_model()

class Profile(models.Model):
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    members = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    is_trainer = models.BooleanField(default=False)