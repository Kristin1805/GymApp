from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from rest_framework import serializers

from GymApp.membership.models import MembershipPlan
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from GymApp.membership.serializers import MembershipListSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView

def is_it_a_trainer(value):
    if value.__class__.__name__ == 'Trainer':
        return True

    return False


@permission_required('admin.add_trainer')
def create_membership_plan(request):
    form = CreateMembershipForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("memberships/plans.html")

    return render(request=request, template_name="memberships/create_membership_plan.html", context={"form": form})

class AllClassesListView(ListAPIView):
    queryset = MembershipPlan.objects.all()
    serializer_class = MembershipListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]



class MembershipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlan
        fields = ['plan', 'img', 'price', 'workouts',
                  'trainer']