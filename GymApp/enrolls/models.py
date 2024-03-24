from django.db import models

from GymApp.membership.models import MembershipPlan
from GymApp.people.models import People


# Create your models here.
class Enroll(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    membershipplan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)