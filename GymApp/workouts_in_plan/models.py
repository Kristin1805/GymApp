from django.db import models




class Workout(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()  # Assuming duration is in minutes
    image = models.ImageField(upload_to='workout_images/', blank=True, null=True)
    instructions = models.TextField()
    video_url = models.URLField(null=True, blank=True)


# class WorkoutsPlans(models.Model):
#