from django.contrib.auth.decorators import login_required, permission_required
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

class TrainerDeleteView(DeleteView, LoginRequiredMixin):
    model = USER_MODEL
    template_name = "trainers/deletetrainer.html"
    success_url = reverse_lazy("home")



@login_required
@permission_required('trainers.can_add_workout', raise_exception=True)
def add_workout(request):
    # Your code to add workout program
    pass

@login_required
@permission_required('trainers.can_delete_workout', raise_exception=True)
def delete_workout(request, workout_id):
    # Your code to delete workout program
    pass

@login_required
@permission_required('trainers.can_change_workout', raise_exception=True)
def edit_workout(request, workout_id):
    # Your code to edit workout program
    pass


#
# def trainer_payments(request):
#     trainer=Trainer.objects.get(pk=request.session['trainerid'])
#     trainer_pays=TrainerSalary.objects.filter(trainer=trainer).order_by('-id')
#     return render(request, 'trainer/trainer_payments.html',{'trainer_pays':trainer_pays})
