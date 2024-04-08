from django import forms

class PaymentForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    card_number = forms.IntegerField(label='Bank')




# class EnrollForm(forms.ModelForm):
#     class Meta:
#         model = Enroll
#         fields = ['person', 'membershipplan']
#         widgets = {
#             'membershipplan': forms.HiddenInput(),  # Hide the membership plan field
#         }
#


