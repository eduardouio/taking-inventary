from django.test import TestCase
from sap_migrations.lib import DetailMigrationSAP
from accounts.models.CustomUserModel import CustomUserModel


class TESTDetailMigrationSAP(TestCase):
    
    def test_get_fly_report(self):
        user = CustomUserModel.get('eduardo')
        fly_report = DetailMigrationSAP()
        report = fly_report.get(1)
        spected_data = {
            'user': '',
            'takings': []
        }
        self.assertIsInstance(report['user'], dict)
        self.assertIsInstance(report['takings'], list)
        self.assertEqual(
            report['takings'],
            spected_data['takings']
        )
