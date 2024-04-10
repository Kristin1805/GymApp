from django import forms
from .models import Plan
from ..workouts_in_plan.models import Workout


class BasePlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('__all__')

class AddPlanForm(BasePlanForm):
    ...

class EditPlanForm(BasePlanForm):
    ...

