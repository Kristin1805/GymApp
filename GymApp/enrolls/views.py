from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from GymApp.enrolls.forms import PaymentForm
from GymApp.profiles.models import Profile
from GymApp.workouts.models import Plan


@login_required
def fake_payment_view(request, plan_id):
    plan = Plan.objects.get(pk=plan_id)
    # Render the fake payment template with the plan details
    return render(request, 'enrollment/fake_payment.html', {'plan': plan})

@login_required
def checkout(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    user_profile = Profile.objects.get(user=request.user)
    error_message = ''

    if request.method == 'POST':
        form = PaymentForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            card_number = form.cleaned_data['card_number']



            if username == request.user.username and card_number == user_profile.card_num:
                user_profile.paid_plans.add(plan)
                user_profile.save()
                print("Form is valid")
                return redirect('home')  # Redirect to success page
            else:
                error_message = 'You made a mistake.'
        else:
            error_message = 'Form is not valid.'

    form = PaymentForm()
    # If there's an error message, render the form with the error message
    # Otherwise, render the form without any errors
    return render(request, 'enrollment/fake_payment.html', {'user_profile': user_profile, 'error_message': error_message})