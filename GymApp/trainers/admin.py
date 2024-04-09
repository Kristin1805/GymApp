from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from GymApp.trainers.models import Trainer
from django.contrib import admin

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['user', 'salary']  # Customize displayed fields
    search_fields = ['user__username']  # Add search functionality

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Check if user is now a trainer and grant permissions accordingly
        if 'is_trainer' in form.changed_data and obj.is_trainer:
            trainer_group, _ = Group.objects.get_or_create(name='Trainers')
            content_type = ContentType.objects.get_for_model(Trainer)
            permissions = Permission.objects.filter(content_type=content_type)
            for permission in permissions:
                obj.user.user_permissions.add(permission)
            obj.user.groups.add(trainer_group)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user.is_superuser:
            return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user.is_superuser:
            return True
        return super().has_delete_permission(request, obj)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return super().has_add_permission(request)

