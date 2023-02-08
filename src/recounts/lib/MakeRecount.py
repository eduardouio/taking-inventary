import json

from django.core.serializers import serialize

from products.models import Product
from takings.models import TakinDetail, Taking
from recounts.models import RecountTakings, RecountDetails


class MakeRecount():
    ''' 
        Habilita el item para un nuevo conteo, genera una copia 
        del conteo original en un json
        consolida las cantidades
        elimina los registros de las tomas
    '''
    def make(self, id_taking, account_code):
        product = Product.get(account_code)
        taking = Taking.get(id_taking)
        details = TakinDetail.objects.filter(
            id_taking=id_taking
        ).filter(account_code=account_code)
        
        recount = RecountTakings.objects.create(
            id_taking = taking
        )
        consolidate = self.consolitate(recount, product, details)

        if consolidate:
            for item in details:
                item.delete()

    def consolidate(self, recount, product, details):
        report = []
        for item in details:
            report.append({
                'detail': json.loads(serialize('json', [item]))[0],
                'team':  {
                    'manager': '{} {}'.format(
                                        item.id_team.manager.first_name,
                                        item.id_team.manager.last_name),
                    'assistant': item.id_team.warenhouse_assistant,
                    'username': item.id_team.manager.username,
                },
            })

        consolidate = {
            'id_recount_taking': recount,
            'account_code': Product,
            'taking_total_boxes':0,
            'taking_total_bottles':0,
            'quantity': 0,
        }

        for item in details:
            consolidate['taking_total_boxes'] += item.taking_total_boxes
            consolidate['taking_total_bottles'] += item.taking_total_bottles
            consolidate['quantity'] += item.quantity
        
        consolidate.update({'detail', json.dumps(report)})
        RecountDetails.objects.create(**consolidate)
        return True