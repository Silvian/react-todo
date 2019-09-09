import factory
from factory.django import DjangoModelFactory

from .models import Reminder


class ReminderFactory(DjangoModelFactory):
    """Reminder factory."""

    name = factory.Faker('name')
    description = factory.Faker('text')
    completed = False

    class Meta:
        model = Reminder
