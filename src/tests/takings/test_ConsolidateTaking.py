from django.test import TestCase
from takings.lib import ConsolidateTaking
from takings.models import TakinDetail, Taking


class TESTConsolidateTaking(TestCase):

    def test_get_report(self):
        spected = {
            'taking': None
        }