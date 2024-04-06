# views.py
from django.contrib import messages
from django.contrib.auth import authenticate,  logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView

from GymApp.profiles.forms import CreateUser, ProfileEditForm, ProfileDetailsForm, CustomUserEditForm, UserProfileForm
from GymApp.profiles.models import USER_MODEL, Profile


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

# class UserDetailsView(DetailView, LoginRequiredMixin):
#     model = USER_MODEL
#     template_name = "profiles/profiledetails.html"
#     context_object_name = "user"
#     custom_context = {"logged": True}
#
#     def post(self, request, *args, **kwargs):
#         form = ProfileDetailsForm(request.POST, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile_details')  # Redirect to the same page or update as needed
#         else:
#             context = self.get_context_data()
#             context['form'] = form
#             return self.render_to_response(context)
#
#     def get_object(self, queryset=None):
#         return self.request.user

@login_required
def profile_details(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None
    return render(request, 'profiles/profiledetails.html', {'user': user, 'profile': profile})
# class UserProfileUpdateView(UpdateView, LoginRequiredMixin):
#     form_class = ProfileEditForm
#     template_name = "profiles/profile_edit.html"
#     success_url = reverse_lazy("profile")
#     custom_context = {"logged": True}
#
#     def get_object(self, queryset=None):
#         return self.request.user.profile
#
#     def form_valid(self, form):
#         profile_form = ProfileEditForm(self.request.POST, instance=self.request.user.profile)
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect('profile_details')
#
#         else:
#             profile_form = ProfileEditForm(instance=self.request.user.profile)
#


    #
    # def get_context_data(self, **kwargs) -> dict[str, any]:
    #     context = super().get_context_data(**kwargs)
    #     context["customusereditform"] = CustomUserEditForm(instance=self.request.user)
    #     context.update(self.custom_context)
    #     return context

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'profiles/profile_edit.html', {'form': form})


class UserDeleteView(DeleteView, LoginRequiredMixin):
    model = USER_MODEL
    success_url = reverse_lazy('home')
    custom_context = {"logged": True}

    def get_object(self, queryset=None):
        return self.request.user

