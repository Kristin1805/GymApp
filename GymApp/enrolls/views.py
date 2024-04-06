import stripe
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.loader import get_template

from GymApp.enrolls.forms import EnrollForm
# from GymApp.enrolls.models import Enroll, Subscription
from GymApp.membership.models import MembershipPlan

from django.contrib.auth.decorators import login_required


# @login_required
# def enroll(request):
#     if request.method == 'POST':
#         form = EnrollForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('enrollment/success_url')  # Redirect to a success URL after enrollment
#     else:
#         form = EnrollForm()
#
#     # Fetch all people and membership plans
#     all_people = People.objects.all()
#     all_membership_plans = MembershipPlan.objects.all()
#
#     context = {
#         'form': form,
#         'people': all_people,
#         'membership_plans': all_membership_plans,
#     }
#     return render(request, 'enrollment/enroll.html', context)

# @login_required
# def enrollment_view(request):
#     enrollments = Enroll.objects.filter(person=request.profile.people.id).all()
#     enrollments_total = enrollments.count()
#
# #     return render(request, template_name='enrollment/all_enrolled_memberships.html',
# #                   context={'enrollments': enrollments, 'total': enrollments_total})
#
# @login_required
# def enrollment_delete(request, pk):
#     enrollment = Enroll.objects.get(pk=pk)
#     context = {'enrollment': enrollment}
#     if request.method == 'GET':
#         return render(request, 'enrollment/delete_enroll.html', context)
#
#     enrollment.delete()
#     messages.success(request, 'You disenroll your membership plan successfully.')
#
#     return redirect('enrollment/all_enrolled_memberships')
#
# def checkout_enrollment(request, enrollment_id):
#     enrollment= Enroll.objects.get(pk=enrollment_id)
#     return render(request, 'enrollment/checkout.html',{'enrollment': enrollment,})

# def checkout_session(request, enrollment_id):
#     membership= Enroll.objects.get(pk=enrollment_id)
# 	session=stripe.checkout.Session.create(
# 		payment_method_types=['card'],
# 		line_items=[{
# 	      'price_data': {
# 	        'currency': 'inr',
# 	        'product_data': {
# 	          'name': membership.title,
# 	        },
# 	        'unit_amount': membership.price*100,
# 	      },
# 	      'quantity': 1,
# 	    }],
# 	    mode='payment',
#
# 	    success_url='http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}',
# 	    cancel_url='http://127.0.0.1:8000/pay_cancel',
# 	    client_reference_id=enrollment_id
# 	)
# 	return redirect(session.url, code=303)

# Success
#
# from django.core.mail import EmailMessage
#
# def pay_success(request):
# 	session = stripe.checkout.Session.retrieve(request.GET['session_id'])
# 	plan_id=session.client_reference_id
# 	plan= MembershipPlan.objects.get(pk=plan_id)
# 	user=request.user
# 	Subscription.objects.create(
# 		plan=plan,
# 		user=user,
# 		price=plan.price
# 	)
# 	subject='Order Email'
# 	html_content=get_template('enrollment/ordermail.html').render({'title':plan.title})
# 	from_email='codeartisanlab2607@gmail.com'
#
# 	msg = EmailMessage(subject, html_content, from_email, ['john@gmail.com'])
# 	msg.content_subtype = "html"  # Main content is now text/html
# 	msg.send()
#
# 	return render(request, 'homepage.html')
#
# def pay_cancel(request):
# 	return render(request, 'enrollment/cancel.html')
