from django import forms
from .models import Plan

class BasePlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('__all__')

class AddPlanForm(BasePlanForm):
    ...

class EditPlanForm(forms.ModelForm):
    ...
