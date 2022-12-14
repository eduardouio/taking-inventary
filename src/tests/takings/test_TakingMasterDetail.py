from django.test import TestCase
from accounts.models.CustomUserModel import CustomUserModel


class TESTTakingMasterDetailTV(TestCase):

    def setUp(self):
        self.path = '/taking/master-detail/64'
        self.user = CustomUserModel.get(username='eduardo')
        return super().setUp()
    
    def test_get(self):
        self.client.login(username='eduardo', password='1234.abc')
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('takings/taking-detail.html')
        self.assertEqual(response.context_data['title_page'], 'Detalle Toma 64')
    
    def test_not_logged(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 302)
        