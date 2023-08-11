import pytest

from recounts.lib import MakeRecount
from recounts.models import RecountDetails, RecountTakings
from takings.models import Taking, TakinDetail
from takings.lib import ConsolidateTaking
from products.models import Product


@pytest.mark.django_db
class TestMakeRecount:

    def setup_method(self):
        self.maker = MakeRecount()

    def test_recount_taking_with_out_details(self):
        # primero abrimos una toma
        taking = Taking.get(175)
        taking.is_active = True
        taking.save()
        status_recount = self.maker.make(175, '')
        assert status_recount is False
        assert self.maker.make(175, '01012114380113010750') is False

    def test_make_recount_taking_not_found(self):
        assert self.maker.make(0, '') is False
    
    def test_make_recount_taking_not_active(self):
        self.maker.make(42, '') is False
    
    def test_recount_data(self):
        before_all_recounts = RecountTakings.objects.filter(id_taking=170).count()
        taking = Taking.get(170)
        taking.is_active = True
        taking.save()
        status_recount = self.maker.make(170, '')
        assert status_recount is True
        afer_all_recounts = RecountTakings.objects.filter(id_taking=170).count()
        # comprobamos la creacion del reconteo
        assert afer_all_recounts -1  == before_all_recounts

        # verificamos los items del reconteo
        last_recount = RecountTakings.objects.filter(id_taking=170).latest('id_recount_taking')
        # verificamos la toma
        assert last_recount.id_taking ==  taking

        # verificamos los items del reconteo son 14 items en la base 
        # para la toma 170
        recount_details = RecountDetails.objects.filter(id_recount_taking=last_recount.pk)
        assert len(recount_details) == 14

        spected_recounts = [
            {
                'account_code': '01011010040217010750',
                'taking_total_boxes': 0,
                'taking_total_bottles': 4,
                'quantity': 4,
                'len_report': 1,
            },
            {
                'account_code': '04015930720101990330',
                'taking_total_boxes': 0,
                'taking_total_bottles': 11,
                'quantity': 11,
                'len_report': 1,
            },{
                'account_code': '01012113620707010750',
                'taking_total_boxes': 0,
                'taking_total_bottles': 4,
                'quantity': 4,
                'len_report': 1,
            },
            {
                'account_code': '01011080010113010750',
                'taking_total_boxes': 0,
                'taking_total_bottles': 6,
                'quantity': 6,
                'len_report': 2,
            }
        ]

        for item in recount_details:
            for spect in spected_recounts:
                if item.account_code.account_code == spect['account_code']:
                    assert item.taking_total_boxes == spect['taking_total_boxes']
                    assert item.taking_total_bottles == spect['taking_total_bottles']
                    assert item.quantity == spect['quantity']
                    assert len(item.detail) == spect['len_report']
                    break
        # veirificamos que no haya tomas pendientes
        report = ConsolidateTaking().get(170)
        report = [x for x in report if x['is_complete'] is False]
        assert len(report) == 43

        # veirificamos que los sample items no tengan tomas
        for item in recount_details:
            product = Product.get(item.account_code)
            assert TakinDetail.objects.filter(account_code=product).count() == 0
    
    def test_recount_one_item(self):
        taking = Taking.get(63)
        taking.is_active = True
        taking.save()
        status_recount = self.maker.make(63, '01011080010402011000')
        product = Product.get('01011080010402011000')
        assert status_recount is True
        taking_details = TakinDetail.objects.filter(
            id_taking=taking,
            account_code=product
            ).count()
        assert taking_details == 0

    def recount_completed_item(self):
        # items completos no se recuentan 
        Taking.get(170).is_active = True
        Taking.get(170).save()
        assert self.maker.make(170, '02012133730306020700') == False
