from cgi import test
from hashlib import new
from unicodedata import name
from django.contrib.auth import get_user_model
from django.test import TestCase
import string
import random

from faker import Faker


class TestAccounts(TestCase):
    
    def setUp(self) -> None:
        self.faker = Faker('es_ES')
        self.User = get_user_model()
        return super().setUp()
    
    def test_create_user(self):
        new_user = self.get_user_data()
        user = self.User.objects.create_user(
            new_user['username'],
            new_user['password'],
            **new_user['extra_fields']
        )
        self.assertEqual(user.email, new_user['extra_fields']['email'])
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        new_user = self.get_user_data()
        user = self.User.objects.create_superuser(
            new_user['username'],
            new_user['password'],
            **new_user['extra_fields']
        )
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.email, new_user['extra_fields']['email'])
    
    def test_fail_user_creation(self):
        new_user = self.get_user_data()
        try:
            new_user['username'] = ''
            user = self.User.objects.create_superuser(
                new_user['username'],
                new_user['password'],
                **new_user['extra_fields']
            )
        except ValueError as err:
            self.assertEqual(
                'The username must be set',
                str(err)
            )
        else:
            self.assertTrue(False)

    def get_user_data(self):
        names = self.faker.name().split(' ')
        new_user  = {
            'username': ''.join(random.choices(string.ascii_letters, k=12)),
            'password': ''.join(random.choices(string.ascii_letters, k=18)),
            'extra_fields': {   
                'first_name': names[0],
                'last_name': ' '.join(names[1:]),
                'email': self.faker.email(),
                'position': 'asistente',
            }
        }
        return new_user
        