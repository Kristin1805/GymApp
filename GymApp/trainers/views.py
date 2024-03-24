from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView

from GymApp.profiles.forms import CreateUser
from GymApp.profiles.models import USER_MODEL


def singup(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after successful signup
    else:
        form = CreateUser()
    return render(request, 'singup.html', {'form': form})




class TrainerLoginView(LoginView):
    template_name = "singup.html"
    success_url = reverse_lazy("home")

class TrainerDetailsView(DetailView, LoginRequiredMixin):
    model = USER_MODEL
    template_name = "trainers/trainerdetails.html"
    context_object_name = "user"

    def get_object(self, queryset=None):
        return self.request.user

class TrainerDeleteView(DeleteView, LoginRequiredMixin):
    model = USER_MODEL
    template_name = "trainers/deletetrainer.html"
    success_url = reverse_lazy("home")



