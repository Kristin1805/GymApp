from django.urls import path
from django.views.generic import TemplateView

from GymApp.enrolls.views import fake_payment_view, checkout




urlpatterns = [
    path('training-plan/<int:plan_id>/fake-payment/', checkout, name='fake_payment'),
    path('process-payment/<int:plan_id>/', checkout, name='process_payment'),
    path('payment-success/', TemplateView.as_view(template_name='enrollment/payment_success.html'), name='payment_success'),
    path('payment-error/', TemplateView.as_view(template_name='enrollment/payment_error.html'), name='payment_error'),
]
