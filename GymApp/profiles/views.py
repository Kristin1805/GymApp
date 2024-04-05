# views.py
from django.contrib import messages
from django.contrib.auth import authenticate,  logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView

from GymApp.profiles.forms import CreateUser, ProfileEditForm
from GymApp.profiles.models import USER_MODEL




class UserRegistrationView(CreateView):
    form_class = CreateUser
    template_name = "signup.html"
    success_url = reverse_lazy("home")
    custom_context = {"logged": False}
    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context.update(self.custom_context)
        return context


class UserLoginView(LoginView):
    template_name = "signin.html"
    success_url = reverse_lazy("home")
    custom_context = {"logged": False}

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context.update(self.custom_context)
        return context

class UserDetailsView(DetailView, LoginRequiredMixin):
    model = USER_MODEL
    template_name = "profiles/profiledetails.html"
    context_object_name = "user"
    custom_context = {"logged": True}

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context.update(self.custom_context)
        return context

    def get_object(self, queryset=None):
        return self.request.user



class UserProfileUpdateView(UpdateView, LoginRequiredMixin):
    form_class = ProfileEditForm
    template_name = "profiles/profile_edit.html"
    success_url = reverse_lazy("profile")
    custom_context = {"logged": True}

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context.update(self.custom_context)
        return context


class UserDeleteView(DeleteView, LoginRequiredMixin):
    model = USER_MODEL
    success_url = reverse_lazy('home')
    custom_context = {"logged": True}

    def get_object(self, queryset=None):
        return self.request.user

