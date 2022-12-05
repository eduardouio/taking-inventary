import json
from datetime import datetime
from django.core.serializers import serialize
from django.views.generic import TemplateView

from sap_migrations.lib import ConsolidateMigration
from sap_migrations.models import SapMigration
from warenhouses.models import Warenhouse
from accounts.models import Team
from takings.models import Taking
from accounts.models import CustomUserModel
from django.http import HttpResponse


# /taking/select/<int:id_sap_migration>/ 
class CreateTakingTP(TemplateView):
    template_name = 'takings/create-taking.html'

    def get(self, request, id_sap_migration, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        report_migration = ConsolidateMigration().get(id_sap_migration) 
        all_warenhouses = self.__get_warenhouses_detail(report_migration)
        all_users = CustomUserModel.objects.all()
        all_users = [{
                'username':i.username,
                'first_name': i.first_name,
                'last_name': i.last_name,
                'role': i.role,
                'is_selected': False} 
            for i in all_users if i.role == 'asistente'
         ]
        page_data = {
            'title_page': 'Custom Taking',
            'module_name': 'Tomas Inventario',
            'pk': id_sap_migration,
            'report_migration': report_migration,
            'all_users': json.dumps(all_users),
            'all_warenhouses': json.dumps(all_warenhouses),
        }
        return self.render_to_response({**context, **page_data})
    
    def post(self, request, id_sap_migration, *args, **kwargs):
        all_takings = Taking.objects.filter(is_active=True)
        for my_taking in all_takings:
            my_taking.is_active = False
            my_taking.save()

        taking = Taking.objects.create(
            id_sap_migration=SapMigration.get(id_sap_migration),
            user_manager=request.user,
            hour_start=datetime.now(),
        )
        for (idx, username) in enumerate(request.POST.get('users').split(',')):
            my_manager = CustomUserModel.get(username)
            if my_manager is None:
                raise Exception('Manager de Equipo no registrado')
            my_team = Team.objects.create(
                manager=my_manager,
                group_number=idx+1,
            )
            taking.teams.add(my_team)

        for (idx, warenhouse) in enumerate(request.POST.get('warenhouses').split(',')):
            my_warenhouse = Warenhouse.get_by_name(warenhouse)
            if my_warenhouse is None:
                raise Exception('La Bodega no existe')
            taking.warenhouses.add(my_warenhouse)

        taking.save()
        return HttpResponse(json.dumps({
                'id_taking': taking.pk})
        , status=201)

    def __get_warenhouses_detail(self, report_migration):
        warenhouses = []
        for wrhs in report_migration['by_warenhouses']:
            my_warenhouse = {
                'detail': json.loads(serialize(
                    'json', 
                    [Warenhouse.get_by_name(wrhs['name'])])
                )[0],
                'owners': Warenhouse.get_owners(wrhs['name']),
                'is_selected': False,
            }
            warenhouses.append({ ** my_warenhouse, ** wrhs['totals']})

        return warenhouses


