from django.shortcuts import render

from GymApp.profiles.models import Profile


# Create your views here.
def home(request):
    return render(request, 'homepage.html')



def login(request):
    return render(request, 'login.html')