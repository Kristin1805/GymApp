# urls.py
from django.urls import path, include
from django.contrib.auth.views import LogoutView


from GymApp.profiles.views import UserRegistrationView, UserLoginView, update_profile, profile_details

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('signin/', UserLoginView.as_view(), name='signin'),
    path("profile_details/", profile_details, name="profile_details"),
    path("edit_profile/",  update_profile, name="profile_edit"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),

]
