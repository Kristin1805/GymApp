from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.http import Http404
from django.shortcuts import render
from .models import Plan
from .views import view_all_plans


class PlanViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test_user', password='password')
        self.plan = Plan.objects.create(subscription_type='gym', amount='100', duration='1 month')

    def test_view_all_plans(self):
        url = reverse('all_plans')
        request = self.factory.get(url)
        response = view_all_plans(request)
        self.assertEqual(response.status_code, 200)  # Should return success

      