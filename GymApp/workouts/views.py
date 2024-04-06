from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from GymApp.workouts.forms import AddPlanForm, EditPlanForm
from GymApp.workouts.models import Plan


# Create your views here.
@login_required
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
def edit_plan(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    if request.method == 'POST':
        form = EditPlanForm(request.POST, request.FILES, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('all_plans')
    else:
        form = EditPlanForm(instance=plan)

    return render(request, 'workouts/edit_plan.html', {'form': form})


@login_required
def delete_plan(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    if request.method == 'POST':
        plan.delete()
        return redirect('all_plans')

    return render(request, 'workouts/delete_plan.html', {'plan': plan})


def all_plans(request):
    plans = Plan.objects.all()
    return render(request, 'workouts/all_plan.html', {'plans': plans})

