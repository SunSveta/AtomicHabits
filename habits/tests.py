from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User
from habits.models import Habit


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User(email='admin@sky.pro')
        self.user.set_password('UNloCKed')
        self.user.is_superuser = True
        self.user.save()

        response = self.client.post("/users/api/token/", {"email": "admin@sky.pro", "password": "UNloCKed"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_habit_create(self):
        response = self.client.post('/habits/create/', {
            "place": "park",
            "time": "20:30",
            "action": "walking",
            "pleasant_habit": "True",
            "frequency": 5,
            "time_to_complete": "00:02",
            "status": "private"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_update(self):
        self.test_habit_create()

        response = self.client.put('/habits/update/4/', {
            "place": "I follow the Moskva down to Gorky Park",
            "time": "20:30",
            "action": "Listening to the wind of change",
            "pleasant_habit": "True",
            "frequency": 5,
            "time_to_complete": "00:02",
            "status": "private"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = {"id": 4, "place": "I follow the Moskva down to Gorky Park", "time": "20:30:00",
            "action": "Listening to the wind of change",
            "pleasant_habit": True,
            "frequency": 5,
            "bonus": None,
            "time_to_complete": "00:02:00",
            "status": "private",
            "related_habit": None}
        self.assertEqual(response.json(), expected_data)

    def test_habit_detail(self):
        self.test_habit_create()

        response = self.client.get('/habits/retrieve/3/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_delete(self):
        self.test_habit_create()

        response = self.client.delete('/habits/destroy/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)