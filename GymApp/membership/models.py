from django.db import models

from GymApp.trainers.models import Trainer
from GymApp.workouts.models import Workout

# Create your models here.
class MembershipPlan(models.Model):
    plan = models.CharField(max_length=180)
    img = models.ImageField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    workouts = models.ManyToManyField(Workout)
    # trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
