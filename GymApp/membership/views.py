from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.decorators import login_required, user_passes_test
from GymApp.membership.models import MembershipPlan
from GymApp.trainers.forms import CreateMembershipForm


def is_it_a_trainer(value):
    if value.__class__.__name__ == 'Trainer':
        return True

    return False


@login_required
@user_passes_test(is_it_a_trainer)
def create_membership_plan(request):
    form = CreateMembershipForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("memberships/plans.html")

    return render(request=request, template_name="memberships/create_membership_plan.html", context={"form": form})

