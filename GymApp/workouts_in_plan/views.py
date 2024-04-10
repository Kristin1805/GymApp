from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from GymApp.profiles.models import PlanWorkout
from GymApp.workouts.models import Plan
from GymApp.workouts_in_plan.forms import AddWorkoutForm, EditWorkoutForm
from GymApp.workouts_in_plan.models import Workout


# Create your views here.
@login_required
@permission_required('trainers.can_add_workout', raise_exception=True)
def add_workout(request):
    if request.method == 'POST':
        form = AddWorkoutForm(request.POST, request.FILES)

        if form.is_valid():
            plan_id = form.cleaned_data['plan'].id
            workout_name = form.cleaned_data['name']
            duration = form.cleaned_data['duration']
            image = form.cleaned_data['image']
            instructions = form.cleaned_data['instructions']

            try:
                plan = Plan.objects.get(id=plan_id)
            except Plan.DoesNotExist:
                messages.error(request, 'Plan with ID {} does not exist'.format(plan_id))
                return redirect('home')

            workout = Workout.objects.create(name=workout_name, duration=duration, image=image, instructions=instructions)


            plan_workout = PlanWorkout(plan=plan, workout=workout)
            plan_workout.save()

            messages.success(request, 'Workout added successfully!')
            return redirect('home')

    else:
        form = AddWorkoutForm()

    return render(request, 'workouts/add_workout.html', {'form': form})


@login_required
@permission_required('trainers.can_edit_workout', raise_exception=True)
def edit_workout(request, workout_id):
    try:
        workout = Workout.objects.get(pk=workout_id)
    except Workout.DoesNotExist:
        messages.error(request, 'Workout with ID {} does not exist'.format(workout_id))
        return redirect('home')

    if request.method == 'POST':
        form = EditWorkoutForm(request.POST, request.FILES, instance=workout)

        if form.is_valid():
            form.save()
            messages.success(request, 'Workout updated successfully!')
            return redirect('home')
    else:
        form = EditWorkoutForm(instance=workout)

    return render(request, 'workouts/edit_workout.html', {'form': form, 'workout': workout})



@login_required
@permission_required('trainers.can_delete_plan', raise_exception=True)
def delete_plan(request, plan_id):
    plan = get_object_or_404(Workout, pk=plan_id)
    if request.method == 'POST':
        plan.delete()
        return redirect('all_plans')

    return render(request, 'workouts/delete_plan.html', {'plan': plan})


@login_required
@permission_required('trainers.can_delete_workout', raise_exception=True)
def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    if request.method == 'POST':
        workout.delete()
        return redirect('workouts_to_edit')
    return render(request, 'workouts/confirm_delete_workout.html', {'workout': workout})
@login_required
def workouts_to_edit(request, plan_id):

    plan_workouts = PlanWorkout.objects.filter(plan_id=plan_id)

    workouts = [plan_workout.workout for plan_workout in plan_workouts]

    context = {
        'workouts': workouts
    }

    return render(request, 'workouts/edit_workout.html', context)