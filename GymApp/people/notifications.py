
import datetime
from django.db.models import Q
from django.db.models.signals import post_save

from GymApp.people.models import Member


def get_notification_count():
    NOTIF_COUNT = Member.objects.filter(
        registration_upto__gte=datetime.datetime.now(),
        registration_upto__lte=datetime.date.today() + datetime.timedelta(days=1),
        notification=1)
    PENDING_COUNT = Member.objects.filter(fee_status='pending', notification=1)
    return (NOTIF_COUNT | PENDING_COUNT).distinct().count()