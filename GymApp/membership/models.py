from django.db import models

from GymApp.trainers.models import Trainer
from GymApp.workouts.models import Workout


# class Enroll(models.Model):
#     first_name = models.CharField(max_length=25)
#     second_name = models.CharField(max_length=25)
#     email = models.EmailField(blank=False, null=False)
#     gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
#     phone_number = models.CharField(max_length=10)
#     payment_status = models.CharField(max_length=55, blank=False, null=False)
#     due_date = models.DateField(blank=False, null=False)
#     timestamp = models.DateTimeField(auto_now_add=True)


# Create your models here.
class MembershipPlan(models.Model):
    plan = models.CharField(max_length=180)
    img = models.ImageField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    workouts = models.ManyToManyField(Workout)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
