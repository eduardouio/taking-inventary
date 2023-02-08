from django.http import HttpResponseRedirect
from django.views.generic import View

from recounts.lib import MakeRecount
from takings.models import Taking, TakinDetail
from takings.lib import ConsolidateTaking

# /recounts/make/taking/<int:id_taking>/
class MakeRecountView(View):
    # todo verificar los items de los detalles de toma
    def get(self, request, id_taking):
        resume = ConsolidateTaking().get(id_taking)
        for item in resume:
            pass
        import ipdb;ipdb.set_trace()


        

