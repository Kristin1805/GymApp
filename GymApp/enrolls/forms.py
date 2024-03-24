from django import forms
from .models import Enroll


class EnrollForm(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = ['person', 'membershipplan']
        widgets = {
            'membershipplan': forms.HiddenInput(),  # Hide the membership plan field
        }