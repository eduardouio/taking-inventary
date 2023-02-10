from django.test import TestCase

from recounts.lib import MakeRecount
from products.models import Product
from takings.models import TakinDetail, Taking
from recounts.models import RecountTakings, RecountDetails


class TESTMakeRecount(TestCase):

    def test_make(self):
        make_recount = MakeRecount()
        recount = make_recount.make(18)
