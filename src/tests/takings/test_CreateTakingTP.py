from django.test import TestCase
from accounts.models.CustomUserModel import CustomUserModel


class TestCreateTakingTP(TestCase):

    def setUp(self):
        self.path = '/taking/create/13'
        self.user = CustomUserModel.get(username='eduardo')
        return super().setUp()
    
    def test_get(self):
        self.client.login(username='eduardo',password='1234.abc')
        response = self.client.get(self.path)
        self.assertTemplateUsed('takings/create-taking.html')
        self.assertEqual(response.status_code, 200)

    def test_not_lloged(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 302)
    
    def test_post(self):
        pass
