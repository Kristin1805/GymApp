from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from GymApp.profiles.models import Profile

USER_MODEL = get_user_model()


@receiver(post_save, sender=USER_MODEL)
def create_and_save_user_profile(sender, instance, created, **kwargs) -> None:
    if created:
        Profile.objects.get_or_create(user=instance)