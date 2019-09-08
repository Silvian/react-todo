from django.contrib import admin

from .models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "modified",
        "created",
        "completed",
    )
