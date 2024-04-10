from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from GymApp.profiles.models import Profile, PlanWorkout
from GymApp.workouts.forms import AddPlanForm, EditPlanForm
from GymApp.workouts.models import Plan
from GymApp.workouts_in_plan.models import Workout


# Create your views here.
@login_required
@permission_required('trainers.can_add_plan', raise_exception=True)
def add_plan(request):
    if request.method == 'POST':
        form = AddPlanForm(request.POST, request.FILES)
        if form.is_valid():
            plan = form.save()  # Save the plan object

            # Create a PlanWorkout entry for the newly added plan
            plan_workout = PlanWorkout(plan=plan)
            plan_workout.save()

            return redirect('all_plans')
    else:
        form = AddPlanForm()

    return render(request, 'workouts/add_plan.html', {'form': form})
@login_required
@permission_required('trainers.can_edit_plan', raise_exception=True)
def edit_plan(request, plan_id):
    # Fetch the plan object based on plan_id
    plan = get_object_or_404(Plan, id=plan_id)

    if request.method == 'POST':
        form = EditPlanForm(request.POST, request.FILES, instance=plan)
        if form.is_valid():
            form.save()  # Save the updated plan object

            return redirect('all_plans')
    else:
        form = EditPlanForm(instance=plan)

    return render(request, 'workouts/edit_plan.html', {'form': form, 'plan': plan})

@login_required
@permission_required('trainers.can_delete_plan', raise_exception=True)
def delete_plan(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    if request.method == 'POST':
        plan.delete()
        return redirect('all_plans')

    return render(request, 'workouts/delete_plan.html', {'plan': plan})


def plan_workouts_view(request, plan_id):
    try:
        # Retrieve the plan object based on plan_id
        plan = Plan.objects.get(pk=plan_id)
        # Retrieve all related plan-workout instances for the plan
        plan_workouts = PlanWorkout.objects.filter(plan=plan)
        # Extract the workouts from plan_workouts
        workouts = [plan_workout.workout for plan_workout in plan_workouts]
    except Plan.DoesNotExist:
        # Handle the case where the plan does not exist
        # You can raise Http404 or render an appropriate response
        raise Http404("Plan does not exist")

    context = {
        'plan': plan,
        'workouts': workouts
    }

    return render(request, 'workouts/all_workouts_in_plan.html', context)

def view_all_plans(request):
    plans = Plan.objects.all()  # Query all plans from the database
    context = {'plans': plans}
    return render(request, 'workouts/all_plan.html', context)