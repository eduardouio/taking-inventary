from django.test import TestCase


class TestCaseBase(TestCase):
    fixtures = ['tests/test_data/test_seed.json']
