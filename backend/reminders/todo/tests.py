from rest_framework import status
from rest_framework.test import APITestCase

from .factories import ReminderFactory


class RemindersViewSetAPITest(APITestCase):
    """Reminders API Tests."""

    def setUp(self):
        self.reminder = ReminderFactory()
        self.url = "/api/v1/todo/"

    def test_list_reminders(self):
        result = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, result.status_code)

        self.assertEqual(1, len(result.data))
        self.assertEqual(self.reminder.id, result.data[0]["id"])
        self.assertEqual(self.reminder.name, result.data[0]["name"])
        self.assertEqual(self.reminder.description, result.data[0]["description"])
        self.assertEqual(self.reminder.completed, result.data[0]["completed"])

    def test_retrieve_reminder(self):
        reminder = ReminderFactory()
        result = self.client.get(self.url + f"{reminder.id}/")
        self.assertEqual(status.HTTP_200_OK, result.status_code)

        self.assertEqual(reminder.id, result.data["id"])
        self.assertEqual(reminder.name, result.data["name"])
        self.assertEqual(reminder.description, result.data["description"])
        self.assertEqual(reminder.completed, result.data["completed"])

    def test_create_reminder(self):
        name = "Test name"
        description = "Test description"
        request = {
            "name": name,
            "description": description,
            "completed": False,
        }
        result = self.client.post(self.url, data=request)
        self.assertEqual(status.HTTP_201_CREATED, result.status_code)

        self.assertEqual(name, result.data["name"])
        self.assertEqual(description, result.data["description"])
        self.assertFalse(result.data["completed"])

    def test_update_reminder(self):
        request = {
            "name": self.reminder.name,
            "description": self.reminder.description,
            "completed": True,
        }
        result = self.client.put(self.url + f"{self.reminder.id}/", data=request)
        self.assertEqual(status.HTTP_200_OK, result.status_code)

        self.assertEqual(self.reminder.name, result.data["name"])
        self.assertEqual(self.reminder.description, result.data["description"])
        self.assertTrue(result.data["completed"])

    def test_delete_reminder(self):
        result = self.client.delete(self.url + f"{self.reminder.id}/")
        self.assertEqual(status.HTTP_204_NO_CONTENT, result.status_code)
        self.assertIsNone(result.data)

        result = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, result.status_code)
        self.assertEqual(0, len(result.data))
