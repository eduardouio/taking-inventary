import json
from datetime import datetime
from time import time

from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db import connection

from accounts.models.CustomUserModel import CustomUserModel
from accounts.models.Team import Team
from accounts.mixins import ValidateManagerMixin
from sap_migrations.lib import ConsolidateMigration
from sap_migrations.models import SapMigration, SapMigrationDetail
from takings.models import Taking


# /taking/create/<int:id_sap_migration>/
class CreateTakingTP(ValidateManagerMixin, TemplateView):
    template_name = 'takings/create-taking.html'

    def get(self, request, id_sap_migration, *args, **kwargs):
        start_time = time()
        context = self.get_context_data(**kwargs)
        report_migration = ConsolidateMigration().get(id_sap_migration)
        all_warenhouses = self.get_warenhouses(id_sap_migration)
        all_users = CustomUserModel.objects.all()

        all_users = [{
            'username': i.username,
            'first_name': i.first_name,
            'last_name': i.last_name,
            'role': i.role,
            'is_selected': False
        }
            for i in all_users if i.role == 'asistente'
        ]
        page_data = {
            'title_page': 'Custom Taking',
            'module_name': 'Tomas Inventario',
            'pk': id_sap_migration,
            'report_migration': report_migration,
            'all_users': json.dumps(all_users),
            'all_warenhouses': json.dumps(all_warenhouses),
            'total_time': time()-start_time
        }
        return self.render_to_response({**context, **page_data})

    def post(self, request, id_sap_migration, *args, **kwargs):
        taking = Taking.objects.create(
            id_sap_migration=SapMigration.get(id_sap_migration),
            notes=request.POST.get('notes'),
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
                id_taking=taking.pk
            )
            taking.teams.add(my_team)
        warenhouses = list(set(request.POST.get('warenhouses').split(',')))

        taking.total_warenhouses = len(warenhouses)
        taking.total_groups = len(request.POST.get('users').split(','))
        taking.warenhouses = json.dumps(warenhouses)
        taking.save()
        return HttpResponse(json.dumps({
            'id_taking': taking.pk}), status=200)

    def get_warenhouses(self, id_sap_migration):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT 
                DISTINCT(sms.warenhouse_name),
                sms.company_name,
                sms.id_warenhouse_sap_code
            FROM sap_migrations_sapmigrationdetail sms 
            WHERE 
            sms.id_sap_migration_id = {};
        """.format(id_sap_migration))
        columns = [col[0] for col in cursor.description]
        warenhouses = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

        for w in warenhouses:
            w['is_selected'] = False

        return warenhouses
