import json

from takings.models import TakinDetail, Taking
from recounts.models import RecountTakings, RecountDetails
from takings.lib import ConsolidateTaking
from products.models import Product
from api.Serializers import TakingDetailSerializer


class MakeRecount():
    ''' 
        Habilita el item para un nuevo conteo, genera una copia 
        del conteo original en un json  
        consolida las cantidades
        elimina los registros de las tomas
    '''

    def make(self, id_taking, account_code):
        taking = Taking.get(id_taking)

        if taking is None:
            return False

        tk_resume = ConsolidateTaking().get(id_taking)
        tk_resume = [i for i in tk_resume
                     if i['is_complete'] is False
                     ]
        
        if self.checker(taking, account_code, tk_resume) is False:
            return False

        recount = RecountTakings.objects.create(
            id_taking=taking
        )

        # si tenemos un codigo contable especifico solo borramos ese item
        if account_code:
            for item_resume in tk_resume:
                if item_resume['account_code'] == account_code:
                    self.consolidate(item_resume, taking, recount)
                    return True

        # si no tenemos un codigo contable especifico borramos todos los items
        for item_resume in tk_resume:
            self.consolidate(item_resume, taking, recount)

        return True

    def consolidate(self, item_resume, taking, recount):
        # buscamos las tomas del item
        taking_detail = TakinDetail.objects.filter(
            id_taking=taking.pk
        ).filter(account_code=item_resume['id_product'])

        if taking_detail.count() == 0:
            return True

        report = TakingDetailSerializer(taking_detail, many=True).data
        report = [dict(i) for i in report]

        consolidate = {
            'id_recount_taking': recount,
            'account_code': Product.get(item_resume['account_code']),
            'taking_total_boxes': 0,
            'taking_total_bottles': 0,
            'quantity': 0,
            'detail': report
        }

        for detail in taking_detail:
            consolidate['taking_total_boxes'] += detail.taking_total_boxes
            consolidate['taking_total_bottles'] += detail.taking_total_bottles
            consolidate['quantity'] += detail.quantity

        RecountDetails.objects.create(**consolidate)
        [detail.delete() for detail in taking_detail]

        return True

    def checker(self, taking, account_code, tk_resume) -> bool:
        ''' 
            Verifica si la toma tiene detalles
            si tiene detalles no se puede hacer un nuevo conteo
        '''   
        if taking.is_active is False:
            return False

        taking_detail = TakinDetail.objects.filter(
            id_taking=taking.pk
        )

        if taking_detail.count() == 0:
            return False

        if account_code:
            for item_resume in tk_resume:
                if item_resume['account_code'] == account_code:
                    return True
            return False

        return True