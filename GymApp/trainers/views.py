from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView

from GymApp.profiles.forms import CreateUser
from GymApp.profiles.models import USER_MODEL, PlanWorkout
from GymApp.workouts.models import Plan


def singup(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after successful signup
    else:
        form = CreateUser()
    return render(request, 'signup.html', {'form': form})




class TrainerLoginView(LoginView):
    template_name = "signup.html"
    success_url = reverse_lazy("home")

class TrainerDetailsView(DetailView, LoginRequiredMixin):
    model = USER_MODEL
    template_name = "trainers/trainerdetails.html"
    context_object_name = "user"

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all plans
        plans = Plan.objects.all()
        context['plans'] = plans
        return context

class TrainerDeleteView(DeleteView, LoginRequiredMixin):
    model = USER_MODEL
    template_name = "trainers/deletetrainer.html"
    success_url = reverse_lazy("home")

def workouts_to_edit(request, plan_id):
    # Retrieve the plan workouts for the given plan_id
    plan_workouts = PlanWorkout.objects.filter(plan_id=plan_id)

    # Extract the associated workouts from the plan workouts
    workouts = [plan_workout.workout for plan_workout in plan_workouts]

    context = {
        'workouts': workouts
    }

    return render(request, 'trainers/workouts_to_edit.html', context)



#
# def trainer_payments(request):
#     trainer=Trainer.objects.get(pk=request.session['trainerid'])
#     trainer_pays=TrainerSalary.objects.filter(trainer=trainer).order_by('-id')
#     return render(request, 'trainer/trainer_payments.html',{'trainer_pays':trainer_pays})
