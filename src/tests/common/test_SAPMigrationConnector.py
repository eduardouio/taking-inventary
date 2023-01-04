from django.test import TestCase

from common import SAPMigrationConnector


class Test_SAPMigrationConector(TestCase):

	def test_connection(self):
		conn = SAPMigrationConnector()
		migration = conn.runMigration()
		self.assertIsInstance(migration, list)