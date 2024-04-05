# urls.py
from django.urls import path


from GymApp.people.views import view_members, add_member, update_member

urlpatterns = [
    path('add_member/', add_member, name='add_member'),
    path('<int:pk>/view_members/', view_members, name='view_members'),
    path("<int:pk>/update_member/", update_member, name='update_member'),
]
