from django.urls import path

from GymApp.trainers.views import workouts_to_edit
from GymApp.workouts.views import plan_workouts_view
from GymApp.workouts_in_plan.views import add_workout, edit_workout,delete_workout

urlpatterns = [
    path('add_workout/', add_workout, name='add_workout'),
    path('plan/<int:plan_id>/', plan_workouts_view, name='plan_workouts'),
    path('edit_workout/<int:workout_id>/', edit_workout, name='edit_workout'),
    path('workouts_to_edit/<int:plan_id>/', workouts_to_edit, name='workouts_to_edit'),
    path('workout/delete/<int:workout_id>/', delete_workout, name='delete_workout'),
]
