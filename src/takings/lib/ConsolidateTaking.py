from django.core.serializers import serialize
from takings.models import TakinDetail, Taking


class ConsolidateTaking(object):

    def get(self, id_taking):
        report = self.__get_init_report(id_taking)

    def __reduce(self, report, product, condition):
        pass

    def __resume(self, keyword, report):
        pass

    def __get_init_report(self, id_taking):
        report = {
            'taking': None,
            'taking_detail': None,
            'status': False,
            'products': {},
            'warenhouses': {},
            'owners': {},
            'totals':{
                'on_hand': 0
            }
        }

    def __compress_report(self):
        pass
