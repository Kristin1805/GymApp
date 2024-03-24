# urls.py
from django.urls import path, include
from GymApp.profiles.views import singup, UserDetailsView

urlpatterns = [
    path('singup/', singup, name='singup'),
    path('singin/', singup, name='singup'),
    path("profile/", include([path("", UserDetailsView.as_view(), name="profile_details"),]),),
]
