from rest_framework import serializers

from .models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    """Reminders serializer."""

    class Meta:
        model = Reminder
        fields = (
            "id",
            "name",
            "description",
            "completed",
            "created",
            "modified",
        )

        read_only_fields = (
            "id",
            "created",
            "modified",
        )
