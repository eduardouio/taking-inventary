# consolidate takinf and taking detail info
# get user manager
# ger teams whit user manager team

import json
import time
from django.db import connection
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models.CustomUserModel import CustomUserModel
from api.Serializers import (CustomUserSerializer, ProductSerializer,
                             TakingSerializer, TeamSerializer, RecountTakingsSerializer)
from products.models import Product
from takings.lib import ConsolidateTaking
from takings.models import TakinDetail, Taking
from sap_migrations.models import SapMigrationDetail
from recounts.models import RecountTakings



# /api/common/taking-data/<id_taking>/
class AllTakingDataAPIView(APIView):

    def get(self, request, id_taking, *args, **kwargs):
        
        print('TIEMPO INICIAL')
        start_time = time.time()
        print(start_time)

        taking = Taking.get(id_taking)
        if taking is None:
            raise Http404

        # recuperamos reporte consolidado
        detail = ConsolidateTaking().get(id_taking)
        report = []

        print('TIEMPO CONSOLIDADO')
        print(time.time() - start_time)


        # personalizamos reporte
        for item in detail:
            product = ProductSerializer(Product.get(item['account_code'])).data
            delete_fields = [
                'created',
                'modified',
                'is_active',
                'id_user_created',
                'id_user_updated',
                'notes',
                'unit_measurement',
                'sale_unit_measurement',
                'alcoholic_strength',
                'ean_14_code',
                'health_register',
                'image_back',
                'max_stock',
                'min_stock',
                'box_dimensions',
                'product_dimensions',
                'ice_code',
                ]
            
            for field in delete_fields:
                del product[field]

            report.append({
                'product': product,
                'sap_stock': item['total_onhand'],
                'is_complete': item['is_complete'],
                'tk_quantity': item['taking'],
            })

        # recuperamos equipos y creamos el diccionario
        teams = TeamSerializer(taking.teams.all(), many=True).data
        teams = [dict(t) for t in teams]

        for team in teams:
            delete_fields_teams = [
                'created',
                'modified',
                'is_active',
                'id_user_created',
                'id_user_updated',
                'notes',
            ]
            
            for field in delete_fields_teams:    
                del team[field]
            
            team['manager'] = CustomUserSerializer(
                CustomUserModel.objects.get(pk=team['manager'])
            ).data

            delete_fields_manager = [
                'last_login',
                'is_superuser',
                'email',
                'is_staff',
                'is_active',
                'date_joined',
                'role',
                'notes',
                'contact',
                'dni_number',
                'picture',
                'groups',
                'user_permissions',
            ]

            for field in delete_fields_manager:
                del team['manager'][field]
            
            team['selected'] = True
           
        # obtenemos todas las bodegas de la migracion
        all_warenhouses = self.get_all_warenhouses(taking)

        # obtenemos todos los usuarios asistentes
        all_users_assistants = CustomUserModel.objects.filter(
            role='asistente'
        )

        # serializamos el objeto
        all_users_assistants = CustomUserSerializer(
            all_users_assistants, many=True
        ).data

        # creamos el diccionario
        all_users_assistants = [dict(t) for t in all_users_assistants]

        # agregamos campo selected
        for user in all_users_assistants:
            user['selected'] = False
        
        # enterprises
        enterprises = SapMigrationDetail.objects.filter(
            id_sap_migration = taking.id_sap_migration,
        ).filter(   
            warenhouse_name__in=json.loads(taking.warenhouses)
        ).values('company_name').order_by('company_name').distinct()

        # reconteos
        recounts = RecountTakings.objects.filter(id_taking = taking)

        print('TIEMPO FINAL')
        print(time.time() - start_time)

        data = {
            'taking': TakingSerializer(taking).data,
            'teams': teams,
            'enterprises': [e['company_name'] for e in enterprises],
            'report': report,
            'manager': CustomUserSerializer(taking.user_manager).data,
            'all_warenhouses': all_warenhouses,
            'all_users_assistants': all_users_assistants,
            'recounts': RecountTakingsSerializer(recounts, many=True).data,
            'syncs': self.get_syncs(taking),
        }

        return Response(data)
        
    def get_syncs(self, taking):
        syncs = {
            'all': [],
            'groups': [],
        }
        # sincronizaciones
        query = '''
            SELECT DISTINCT ttd.id_team_id, ttd.token_team 
            FROM takings_takindetail ttd 
            WHERE ttd.token_team IN (
	    SELECT DISTINCT(token_team) FROM takings_takindetail where id_taking_id = {})
        '''.format(taking.pk)
        cursor = connection.cursor()
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        syncs['all'] = [dict(zip(columns, row)) for row in cursor.fetchall()]

        query = '''
            SELECT ttd.id_team_id, ttd.created, ttd.token_team
            FROM takings_takindetail ttd
            WHERE (ttd.id_team_id, ttd.created) IN (
                SELECT t2.id_team_id, MAX(t2.created)
                FROM takings_takindetail t2
                WHERE t2.id_taking_id = {}
                GROUP BY t2.id_team_id);
        '''.format(taking.pk)
        cursor = connection.cursor()
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        syncs['groups'] = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return syncs

    def get_all_warenhouses(self, taking):
        query = '''
            SELECT DISTINCT(smd.warenhouse_name) 
            FROM sap_migrations_sapmigrationdetail smd
            WHERE smd.id_sap_migration_id = {};
        '''.format(taking.id_sap_migration.pk)
        cursor = connection.cursor()
        cursor.execute(query)
        used_warenhouses = json.loads(taking.warenhouses)

        data = [{'name': list(row)[0],
                 'selected': False
                 }
                for row in cursor.fetchall() if list(row)[0] not in used_warenhouses
                ]

        used_warenhouses = [{'name': w, 'selected': True} for w in used_warenhouses]
        data = used_warenhouses + data
        cursor.close()
        return data
