from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User(email='admin@sky.pro')
        self.user.set_password('UNloCKed')
        self.user.save()

        response = self.client.post("/users/api/token/", {"email": "admin@sky.pro", "password": "UNloCKed"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_user(self):
        response = self.client.post(path="/users/create_user/",
                                    data={"email": "new_admin@sky.pro", "password": "new_UNloCKed"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

