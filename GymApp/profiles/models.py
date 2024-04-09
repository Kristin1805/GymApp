from django.contrib.auth import get_user_model
from django.db import models

from GymApp.workouts.models import Plan
from GymApp.workouts_in_plan.models import Workout

# Create your models here.
USER_MODEL = get_user_model()

class Profile(models.Model):
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    image = models.FileField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_trainer = models.BooleanField(default=False)
    paid_plans = models.ManyToManyField(Plan, blank=True, null=True, related_name='profile_plans')
    card_num = models.IntegerField(blank=True, null=True)

class PlanWorkout(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, blank=True, null=True)