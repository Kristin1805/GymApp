from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'phone_number', 'user', 'is_trainer']
    list_filter = ('is_trainer',)

    search_fields = ['user__username', 'phone_number']
    def save_model(self, request, obj, form, change):
        # Check if the is_trainer field has been changed
        if 'is_trainer' in form.changed_data:
            # Update the user's profile accordingly
            if obj.is_trainer:
                # Make necessary changes when is_trainer is set to True
                obj.user.is_trainer = True
            else:
                # Make necessary changes when is_trainer is set to False
                obj.user.is_trainer = False
            # Save the user instance to reflect changes
            obj.user.save()
        # Save the profile instance
        obj.save()

