from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GymApp.profiles'

    def ready(self) -> None:
        import GymApp.profiles.signals