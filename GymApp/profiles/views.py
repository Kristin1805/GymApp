# views.py
from django.contrib import messages
from django.contrib.auth import authenticate,  logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView
from django.forms.formsets import formset_factory
from GymApp.profiles.forms import CreateUser, ProfileEditForm, ProfileDetailsForm, CustomUserEditForm, UserProfileForm
from GymApp.profiles.models import USER_MODEL, Profile
from GymApp.workouts.models import Plan


def is_not_trainer(function=None, redirect_url='/all_plans/'):
    """
    Decorator for views that checks if the user is not a trainer.
    If the user is a trainer, they will be redirected to the specified URL.
    """
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
            return redirect('profile_details')  # Redirect to success page
    else:
        user_form = UserProfileForm(instance=request.user)
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileEditForm(instance=profile)
    return render(request, 'profiles/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})

def plan_per_user(request):
    profile = Profile.objects.get(user=request.user)

    return render(request, 'profiles/profiledetails.html', {'profile': profile})


# def plan_detail(request, plan_id):
#     plan = get_object_or_404(Plan, pk=plan_id)
#     workouts = plan.workouts.all()
#     return render(request, 'plan_detail.html', {'plan': plan, 'workouts': workouts})

class UserDeleteView(DeleteView, LoginRequiredMixin):
    model = USER_MODEL
    success_url = reverse_lazy('home')
    custom_context = {"logged": True}

    def get_object(self, queryset=None):
        return self.request.user


class PlanDetailsView(DetailView):
    model = Plan
    template_name = 'workouts/plan_details.html'
    context_object_name = 'plan'