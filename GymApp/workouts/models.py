from django.db import models

from GymApp.workouts_in_plan.models import Workout



# Create your models here.



class Plan(models.Model):
    SUBSCRIPTION_TYPE_CHOICES = (
        ('gym', 'Gym'),
        ('cross_fit', 'Cross Fit'),
        ('gym_and_cross_fit', 'Gym + Cross Fit'),
        ('pt', 'Personal Training')
    )

    subscription_type = models.CharField(max_length=40, choices=SUBSCRIPTION_TYPE_CHOICES)
    amount = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)
    photo = models.FileField(upload_to='photos/', blank=True)

    gym_workouts = models.CharField(max_length=100, blank=True, null=True)
    cross_fit_details = models.TextField(blank=True, null=True)
    personal_training_details = models.CharField(max_length=100,blank=True, null=True)
    personal_training_hours = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.subscription_type
