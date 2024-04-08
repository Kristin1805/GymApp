from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from GymApp.profiles.models import Profile
from GymApp.workouts.forms import AddPlanForm, EditPlanForm
from GymApp.workouts.models import Plan


# Create your views here.
@login_required
@permission_required('trainers.can_add_plan', raise_exception=True)
def add_plan(request):
    if request.method == 'POST':
        form = AddPlanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_plans')
    else:
        form = AddPlanForm()

    return render(request, 'workouts/add_plan.html', {'form': form})


@login_required
@permission_required('trainers.can_delete_plan', raise_exception=True)
def delete_plan(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    if request.method == 'POST':
        plan.delete()
        return redirect('all_plans')

    return render(request, 'workouts/delete_plan.html', {'plan': plan})


def all_plans(request):
    plans = Plan.objects.all()
    return render(request, 'workouts/all_plan.html', {'plans': plans})

def paid_plans_list(request):
    profile = get_object_or_404(Profile, user=request.user)
    paid_plans = profile.paid_plans.all()
    # Serialize paid plans data
    data = [{'id': plan.id, 'subscription_type': plan.subscription_type} for plan in paid_plans]
    return JsonResponse(data, safe=False)


def plan_workouts_view(request, plan_id):
    # Retrieve the plan object based on plan_id
    plan = Plan.objects.get(pk=plan_id)
    # Pass the plan object to the template context
    context = {
        'plan': plan
    }
    # Render the HTML template with the plan's workouts
    return render(request, 'workouts/plan_details.html', context)
