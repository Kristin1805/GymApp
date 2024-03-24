from django import forms
from GymApp.membership.models import MembershipPlan


# Create your views here.
class BaseMembershipForm(forms.ModelForm):
    class Meta:
        model = MembershipPlan
        fields = ['plan', 'img', 'price', 'workouts']
        widgets = {
            "image": forms.URLInput(
                attrs={"placeholder": "https://..."}),
        }

        labels = {
            "plan": "Plan",
            "img": "Image URL",
            "price": "Price",
            "workouts": "workouts",
        }


class CreateMembershipForm(BaseMembershipForm):
    pass


class EditMembershipForm(BaseMembershipForm):
    pass


class DeleteMembershipForm(BaseMembershipForm):
    # Hide ALL Form
    def __init__(self, *args, **kwargs):
        super(DeleteCarForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True


    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()

        return self.instance

