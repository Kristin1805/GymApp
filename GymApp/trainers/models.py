from django.contrib.auth import get_user_model
from django.db import models


USER_MODEL = get_user_model()


class Trainer(models.Model):
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='trainer')
    is_trainer = models.BooleanField(default=True)