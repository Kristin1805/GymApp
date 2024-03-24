from django.db import models

from GymApp.profiles.models import Profile


# Create your models here.
class People(models.Model):
    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    email = models.EmailField(null=False, blank=False)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone_number = models.IntegerField(null=False, blank=False)
    id = models.ForeignKey(Profile, on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
        return self.first_name

