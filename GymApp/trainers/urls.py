# urls.py
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from GymApp.profiles.views import UserRegistrationView, UserLoginView
from GymApp.trainers.views import TrainerDetailsView

urlpatterns = [

    path("<int:pk>/profile/", include([path("", TrainerDetailsView.as_view(), name="trainer_profile_details"),]),),

]

