from django.urls import path

from GymApp.profiles.views import PlanDetailsView
from GymApp.workouts.views import add_plan, delete_plan, all_plans

urlpatterns = [
    path('add_plan/', add_plan, name='add_plan'),
    path('<int:plan_id>/delete/', delete_plan, name='delete_plan'),
    path('all_plans/', all_plans, name='all_plans'),
    path('plan_details/<int:pk>/', PlanDetailsView.as_view(), name='plan_details'),
]