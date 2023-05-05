from django.http import HttpResponseRedirect
from django.views.generic import View

from recounts.lib import MakeRecount


# /recounts/make/taking/<int:id_taking>/product/<str:account_code>
class MakeRecountView(View):
    # todo verificar los items de los detalles de toma
    def get(self, request, id_taking, account_code):
        account_code = account_code if account_code != 'all' else None
        recount = MakeRecount()
        recount.make(id_taking, account_code)

        return HttpResponseRedirect('/takings/detail/{}'.format(id_taking))
