from django.test import TestCase
from sap_migrations.lib import LoadMigration
from sap_migrations.models import SapMigration, SapMigrationDetail


class TESTLoadMigration(TestCase):

	def test_load(self):
		before_count_migrations = SapMigration.objects.all().count()
		before_count_migrations_det = SapMigrationDetail.objects.all().count()
		load_migration = LoadMigration()
		load_migration.load()
		after_count_migrations = SapMigration.objects.all().count()
		after_count_migrations_det = SapMigrationDetail.objects.all().count()
		self.assertEqual(before_count_migrations , after_count_migrations - 1)
		self.assertTrue(before_count_migrations_det < after_count_migrations_det)
