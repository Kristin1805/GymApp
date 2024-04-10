from django.urls import path

# from GymApp.profiles.views import PlanDetailsView
from GymApp.workouts.views import add_plan, delete_plan, view_all_plans, edit_plan

urlpatterns = [
    path('add_plan/', add_plan, name='add_plan'),
    path('<int:plan_id>/delete/', delete_plan, name='delete_plan'),
    path('all_plans/', view_all_plans, name='all_plans'),
    path('edit_plan/<int:plan_id>/', edit_plan, name='edit_plan'),
]
