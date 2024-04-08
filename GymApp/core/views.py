from django.shortcuts import render

from GymApp.profiles.models import Profile


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        logged = True
    else:
        logged = False

    return render(request, 'homepage.html', context={'logged': logged})

def unauthorized_acess(request):
    return render(request, 'homepage.html')