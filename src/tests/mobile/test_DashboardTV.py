from django.test import TestCase

from mobile.views import DashboardTV
from accounts.models.CustomUserModel import CustomUserModel


class TestDashboardTV(TestCase):
    
    def setUp(self):
        self.path = '/mobile/dashboard/'
        return super().setUp()
    
    def test_get(self):
        self.client.login(username='eduardo',password='1234.abc')
        response = self.client.get(self.path)
        self.assertTemplateUsed('mobile/dashboard.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title_page'], 'Dashboar Toma')
    
    def test_not_logged(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 302)
    
