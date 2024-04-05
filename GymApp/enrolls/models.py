# from django.db import models
#
# from GymApp.membership.models import MembershipPlan
#
# from GymApp.profiles.models import Profile
#
#
# # Create your models here.
# class Enroll(models.Model):
#     person = models.ForeignKey(People, on_delete=models.CASCADE)
#     membership_plan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
#
# class Subscription(models.Model):
#     user=models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
#     plan=models.ForeignKey(MembershipPlan, on_delete=models.CASCADE,null=True)
#     price=models.CharField(max_length=50)
#     reg_date=models.DateField(auto_now_add=True,null=True)
