from django.shortcuts import render, redirect

from GymApp.enrolls.forms import EnrollForm
from GymApp.membership.models import MembershipPlan
from GymApp.people.models import People


def enroll(request):
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment/success_url')  # Redirect to a success URL after enrollment
    else:
        form = EnrollForm()

    # Fetch all people and membership plans
    all_people = People.objects.all()
    all_membership_plans = MembershipPlan.objects.all()

    context = {
        'form': form,
        'people': all_people,
        'membership_plans': all_membership_plans,
    }
    return render(request, 'enrollment/enroll.html', context)