# views.py
from django.contrib import messages

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView
from GymApp.profiles.forms import CreateUser, ProfileEditForm, UserProfileForm, ChangePasswordForm
from GymApp.profiles.models import USER_MODEL, Profile



def is_not_trainer(function=None, redirect_url='/all_plans/'):
    actual_decorator = user_passes_test(
        lambda u: not u.profile.is_trainer,
        login_url=redirect_url
    )

    if function:
        return actual_decorator(function)
    return actual_decorator

@login_required
@is_not_trainer
def profile_details(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None
    return render(request, 'profiles/profiledetails.html', {'user': user, 'profile': profile})



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

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileEditForm(request.POST, instance=profile)
        if all([user_form.is_valid(), profile_form.is_valid()]):
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('profile_details')
    else:
        user_form = UserProfileForm(instance=request.user)
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileEditForm(instance=profile)
    return render(request, 'profiles/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})


class UserDeleteView(DeleteView, LoginRequiredMixin):
    model = USER_MODEL
    template_name = 'profiles/delete.html'
    success_url = reverse_lazy('home')
    custom_context = {"logged": True}

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        profile = Profile.objects.get(user=self.object)
        profile.delete()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

@login_required
def change_password(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)


    if request.user != profile.user:
        return redirect('error_page')

    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'profiles/change_password.html', {'form': form, 'user_id': user_id})