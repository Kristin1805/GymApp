from django.db import models
from GymApp.people.models import Member


# Create your models here.
class Payments(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_period = models.IntegerField()
    payment_amount = models.IntegerField()


