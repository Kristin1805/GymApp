# urls.py
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from GymApp.people.views import add_member
from GymApp.profiles.views import UserRegistrationView, UserDetailsView, UserLoginView

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('signin/', UserLoginView.as_view(), name='signin'),
    path("profile/", include([path("", UserDetailsView.as_view(), name="profile_details"),]),),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path('add_member/', add_member, name='add_member'),
]
