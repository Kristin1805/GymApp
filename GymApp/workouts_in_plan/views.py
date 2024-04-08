from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404

from GymApp.workouts.models import Plan
from GymApp.workouts_in_plan.forms import AddWorkoutForm
from GymApp.workouts_in_plan.models import Workout


# Create your views here.
@login_required
@permission_required('trainers.can_add_workout', raise_exception=True)
def add_workout(request):
    if request.method == 'POST':
        form = AddWorkoutForm(request.POST, request.FILES)

        if form.is_valid():

            workout = form.save(commit=False)

            workout.save()  # Save the workout object

            plan_id = request.POST.get('plan')
            try:
                plan = Plan.objects.get(id=plan_id)

            except Plan.DoesNotExist:

                messages.error(request, 'Plan with ID {} does not exist'.format(plan_id))
                return redirect('home')  # Redirect to home or another appropriate URL

            plan.workouts = workout  # Assign the workout object to the plan's workouts field
            plan.save()  # Save the plan object after modifying workouts
            return redirect('home')  # Change 'home' to the name of your home page URL

    else:
        form = AddWorkoutForm()
    return render(request, 'workouts/add_workout.html', {'form': form})
@login_required
@permission_required('trainers.can_delete_plan', raise_exception=True)
def delete_plan(request, plan_id):
    plan = get_object_or_404(Workout, pk=plan_id)
    if request.method == 'POST':
        plan.delete()
        return redirect('all_plans')

    return render(request, 'workouts/delete_plan.html', {'plan': plan})


