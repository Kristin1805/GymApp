from django.urls import path

from GymApp.core import views
from GymApp.core.views import home


urlpatterns = [
    path('', home, name='home'),
]