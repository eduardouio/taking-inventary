from django.test import TestCase
from config.secrets_config import SAP_CONNECTION

from common import SAPMigrationConnector


class Test_SAPMigrationConector(TestCase):

	def test_connection(self):
		conn = SAPMigrationConnector()
		migration = conn.runMigration()
		self.assertIsInstance(migration, list)

	def test_offline_server(self):
		SAP_CONNECTION['server'] = 'donExis'
		conn = SAPMigrationConnector()
		migration = conn.runMigration()
		self.assertFalse(migration)
	
	def test_error_credentials(self):
		SAP_CONNECTION['user'] = 'error'
		SAP_CONNECTION['password'] = 'error'
		conn = SAPMigrationConnector()
		migration = conn.runMigration()
		self.assertFalse(migration)