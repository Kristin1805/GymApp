from django import forms
from django.forms import  ModelForm
from django.shortcuts import redirect, get_object_or_404

from GymApp.payments.models import Payments
from GymApp.people.models import Member, SUBSCRIPTION_TYPE_CHOICES, SUBSCRIPTION_PERIOD_CHOICES, BATCH, FEE_STATUS


class AddMemberForm(ModelForm):
    class Meta:
        model = Member
        # fields = ['first_name', 'last_name', 'mobile_number', 'email', 'address', 'subscription_type', 'subscription_period', 'amount']
        fields = '__all__'
        exclude = ['registration_upto']
        widgets = {
        'registration_date': forms.DateInput(attrs={'class': 'datepicker form-control', 'type': 'date'}),
        'address': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        'medical_history': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        'dob': forms.DateInput(attrs={'class': 'datepicker form-control', 'type': 'date'}),
        'photo': forms.FileInput(attrs={'accept': 'image/*;capture=camera'})
        }
        error_messages = {
            'first_name': {
                'required': 'Please enter first name'
            },
            'last_name': {
                'required': 'Please enter last name'
            },
            'mobile_number': {
                'unique': 'This mobile number has already been registered.'
            }
        }

    def clean_mobile_number(self, *args, **kwargs):
        mobile_number = self.cleaned_data.get('mobile_number')
        if not mobile_number.isdigit():
            raise forms.ValidationError('Mobile number should be a number')

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if not amount.isdigit():
            raise forms.ValidationError('Amount should be a number')
        return amount



class SearchForm(forms.ModelForm):
    search = forms.CharField(label='Search Member', max_length=100, required=False)

    def clean_search(self, *args, **kwargs):
        search = self.cleaned_data.get('search')
        if search == '':
            raise forms.ValidationError('Please enter a name in search box')
        return search

class UpdateMemberGymForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ['registration_date', 'registration_upto', 'subscription_type', 'subscription_period', 'fee_status', 'amount', 'batch']

    registration_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker form-control', 'type': 'date'}),)
    registration_upto = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker form-control', 'type': 'date'}),)

    widgets = {
        'registration_date': forms.DateInput(attrs={'class': 'datepicker form-control', 'type': 'date'}),
        'registration_upto': forms.DateInput(attrs={'class': 'datepicker form-control', 'type': 'date'}),
    }


class UpdateMemberInfoForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'photo', 'dob']

    widgets = {
        'dop': forms.DateInput(attrs={'class': 'datepicker form-control', 'type': 'date'}),
    }