from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from GymApp.trainers.models import Trainer
from django.contrib import admin

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['user', 'salary']  # Customize displayed fields
    search_fields = ['user__username']  # Add search functionality

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Get the content type for Trainer model
        content_type = ContentType.objects.get_for_model(Trainer)

        # Add permission to add, change and delete workout programs only if they don't exist
        if not Permission.objects.filter(codename='can_add_workout', content_type=content_type).exists():
            Permission.objects.create(
                codename='can_add_workout',
                name='Can Add Workout Program',
                content_type=content_type,
            )

        if not Permission.objects.filter(codename='can_change_workout', content_type=content_type).exists():
            Permission.objects.create(
                codename='can_change_workout',
                name='Can Change Workout Program',
                content_type=content_type,
            )

        if not Permission.objects.filter(codename='can_delete_workout', content_type=content_type).exists():
            Permission.objects.create(
                codename='can_delete_workout',
                name='Can Delete Workout Program',
                content_type=content_type,
            )

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
