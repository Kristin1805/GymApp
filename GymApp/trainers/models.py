from django.contrib.auth import get_user_model
from django.db import models

from GymApp.profiles.models import Profile

USER_MODEL = get_user_model()

# Create your models here.
class Trainer(Profile):
    salary = models.DecimalField(max_digits=10, decimal_places=2)
