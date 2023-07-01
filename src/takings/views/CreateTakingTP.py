import json
from datetime import datetime

from django.views.generic import TemplateView
from django.http import JsonResponse
from accounts.mixins import ValidateManagerMixin
from django.http import Http404, HttpResponseBadRequest
from sap_migrations.models import SapMigration
from takings.models import Taking
from accounts.models.Team import Team
from django.contrib.auth import get_user_model


# /takings/create/<int:id_sap_migration>/

UserModel = get_user_model()


class CreateTakingTP(ValidateManagerMixin, TemplateView):
    template_name = 'takings/create-taking.html'

    def get(self, request, id_sap_migration, *args, **kwargs):
        sap_migration = SapMigration.get(
            id_sap_migration=id_sap_migration)

        if sap_migration is None:
            raise Http404('No existe la migración')

        context = super().get_context_data(**kwargs)
        page_data = {
            "id_sap_migration": id_sap_migration
        }

        return self.render_to_response({**context, **page_data})

    def post(self, request, id_sap_migration, *args, **kwargs):
        sap_migration = SapMigration.get(id_sap_migration=id_sap_migration)
        if sap_migration is None:
            raise Http404('No existe la migración')
        try:
            request_data = json.loads(request.body.decode('utf-8'))
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest('JSON inválido')

        # listamos las categorias
        categories = [cat['category'] for cat in request_data['categories']]

        # listamos las bodegas
        warenhouses = [whr['warenhouse']
                       for whr in request_data['warenhouses']]

        # creacion de grupos
        users = [UserModel.get(usr['username'])
                 for usr in request_data['groups']]

        # creamos la toma
        my_taking = Taking.objects.create(
            id_sap_migration=sap_migration,
            hour_start=datetime.now().time(),
            user_manager=request.user,
            name=request_data['name'],
            categories=json.dumps(categories),
            warenhouses=json.dumps(warenhouses),
        )

        # asignamos los usuarios a la toma
        for (idx, user) in enumerate(users):
            my_team = Team.objects.create(
                manager=user,
                group_number=idx+1,
                id_taking=my_taking.pk
            )
            my_taking.teams.add(
                my_team
            )

        # guardamos la toma
        my_taking.save()

        return JsonResponse({
            'id_taking': my_taking.id_taking,
            'message': 'Toma creada correctamente',
        }, status=201)
