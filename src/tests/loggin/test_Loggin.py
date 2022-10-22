from django.test import TestCase
from common import loggin
from config.settings import PATH_LOGS, IS_ENABLE_LOGGIN, LOGS_FILE_NAME
import os


class TestLoggin(TestCase):

    def setUp(self):
        self.file = PATH_LOGS / LOGS_FILE_NAME
        if os.path.exists(self.file):
            os.remove(self.file)

    def test_loggin(self):
        if IS_ENABLE_LOGGIN:
            loggin('i', 'Test de Escritura de datos')
            self.assertEqual(True, os.path.exists(self.file))

    def test_not_loggin(self):
        if not IS_ENABLE_LOGGIN:
            loggin('e', 'No se escribe esto en el archivo')
            self.assertEqual(False, os.path.exists(self.file))
