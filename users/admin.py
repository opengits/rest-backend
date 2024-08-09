from django.contrib import admin
from sharedorm.models import User, Setting  # Adjust import based on where the models are imported from

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'password')

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('is_notification_enabled', 'is_new_dashboard_enabled', 'timezone')
