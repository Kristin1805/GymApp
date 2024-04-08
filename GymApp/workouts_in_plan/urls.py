from django.urls import path

from GymApp.workouts.views import plan_workouts_view
from GymApp.workouts_in_plan.views import add_workout

urlpatterns = [
    path('add_workout/', add_workout, name='add_workout'),
    path('plan/<int:plan_id>/workouts/', plan_workouts_view, name='plan_workouts'),
    # path('<int:plan_id>/delete/', delete_workout, name='delete_plan'),
    # path('all_plans/', all_plans, name='all_plans'),
    # path('plan_details/<int:pk>/', , name='plan_details'),
]