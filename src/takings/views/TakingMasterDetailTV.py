from time import time

from django.views.generic import TemplateView

from takings.lib import ConsolidateTaking
from accounts.mixins import ValidateManagerMixin


# /taking/detail/<int:pk>/
class TakingMasterDetailTV(ValidateManagerMixin, TemplateView):
    template_name = 'takings/taking-detail.html'

    def get(self, request, pk, *args, **kwargs):
        start_time = time()
        context = self.get_context_data(**kwargs)
        report = ConsolidateTaking().get(pk)
        view_all = False

        if request.GET.get('action'):
            action = request.GET.get('action')
            if action == 'open':
                report['taking'].is_active = True

            if action == 'close':
                report['taking'].is_active = False

            report['taking'].save()

            if action == 'view_all':
                view_all = True

        if not view_all:
            report['report'] = [
                x for x in report['report'] if x['diff'] != 0
            ]

        page_data = {
            'id_taking': pk,
            'user': request.user,
            'title_page': 'Toma #{}'.format(pk),
            'module_name': 'Reporte de Toma',
            'taking': report['taking'],
            'teams': report['taking'].teams.all(),
            'report': report['report'],
            'warenhouses': report['warenhouses'],
            'enterprises': report['enterprises'],
            'total_time': time() - start_time,
        }
        return self.render_to_response(context={**context, **page_data})
