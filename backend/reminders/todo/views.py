from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .serializers import ReminderSerializer
from .models import Reminder


class ReminderViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter,)
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all().order_by("-modified")
    search_fields = ("name", "description")
