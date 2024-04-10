from django import forms

from GymApp.workouts.models import Plan
from GymApp.workouts_in_plan.models import Workout


class BaseWorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('__all__')

class AddWorkoutForm(forms.ModelForm):
    plan = forms.ModelChoiceField(queryset=Plan.objects.all(), empty_label=None)

    class Meta:
        model = Workout
        fields = ['name', 'duration', 'image', 'instructions']




class EditWorkoutForm(BaseWorkoutForm):
    ...