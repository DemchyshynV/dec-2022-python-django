from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.users.models import UserModel as User

from ..models import AutoParkModel

UserModel: User = get_user_model()


class AutoParkTestCase(APITestCase):
    def _authenticate(self):
        email = "admin@gmail.com"
        password = "P@$$word1"
        user = {
            "email": email,
            "password": password,
            "profile": {
                "name": "Іван",
                "surname": "Попов",
                "age": 19
            }
        }
        self.client.post(reverse('users_list_create'), user, format='json')
        user = UserModel.objects.get(email='admin@gmail.com')
        user.is_active = True
        user.is_staff = True
        user.save()
        response = self.client.post(reverse('auth_login'), {"email": email, "password": password})
        print(response.status_code)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["access"]}')

    def test_create_auto_park_without_auth(self):
        count = AutoParkModel.objects.count()
        sample_auto_park = {
            'name': 'Uber'
        }
        response = self.client.post(reverse('auto_parks_list_create'), sample_auto_park)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEquals(AutoParkModel.objects.count(), count)

    def test_create_auto_park(self):
        self._authenticate()
        count = AutoParkModel.objects.count()
        sample_auto_park = {
            'name': 'Uber'
        }
        response = self.client.post(reverse('auto_parks_list_create'), sample_auto_park)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.data['name'], 'Uber')
        self.assertIsInstance(response.data['cars'], list)
        self.assertEquals(AutoParkModel.objects.count(), count+1)

