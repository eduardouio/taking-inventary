import json

from django.core.serializers import serialize

from products.models import Product
from takings.models import TakinDetail, Taking
from recounts.models import RecountTakings, RecountDetails
from takings.lib import ConsolidateTaking


class MakeRecount():
    ''' 
        Habilita el item para un nuevo conteo, genera una copia 
        del conteo original en un json  
        consolida las cantidades
        elimina los registros de las tomas
    '''

    def make(self, id_taking, account_code=None):
        taking = Taking.get(id_taking)
        recount = RecountTakings.objects.create(
            id_taking=taking
        )
        tk_resume = ConsolidateTaking().get(id_taking)
        tk_resume = tk_resume['report']
        tk_resume = [i for i in tk_resume
                     if i['sap_stock'] != i['diff'] and i['diff'] != 0
                     ]
        if account_code:
            for item_resume in tk_resume:
                if item_resume.account_code.acount_code == account_code:
                    self.consolidate(item_resume, taking, recount)
                    return True

        for item_resume in tk_resume:
            self.consolidate(item_resume, taking, recount)

        return True

    def consolidate(self, item_resume, taking, recount):
        taking_detail = TakinDetail.objects.filter(
            id_taking=taking.pk
        ).filter(account_code=item_resume['product'])

        report = []
        for detail_tk in taking_detail:
            report.append({
                'detail': json.loads(serialize('json', [detail_tk]))[0]['fields'],
                'team':  {
                    'manager': '{} {}'.format(
                        detail_tk.id_team.manager.first_name,
                        detail_tk.id_team.manager.last_name),
                    'assistant': detail_tk.id_team.warenhouse_assistant,
                    'username': detail_tk.id_team.manager.username,
                },
            })

        consolidate = {
            'id_recount_taking': recount,
            'account_code': item_resume['product'],
            'taking_total_boxes': 0,
            'taking_total_bottles': 0,
            'quantity': 0,
            'detail': json.dumps(report),
        }

        for detail in taking_detail:
            consolidate['taking_total_boxes'] += detail.taking_total_boxes
            consolidate['taking_total_bottles'] += detail.taking_total_bottles
            consolidate['quantity'] += detail.quantity

        RecountDetails.objects.create(**consolidate)

        for taking_det in taking_detail:
            taking_det.delete()

        return True
