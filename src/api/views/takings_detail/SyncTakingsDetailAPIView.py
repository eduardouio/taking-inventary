import json
from datetime import date

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models.Team import Team
from products.models import Product
from takings.models import TakinDetail, Taking

# /api/takings-detail/sync/
class SyncTakingsDetailAPIView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def post(self, request, *args, **kwargs):
        # TODO Testear que pasa sin el getlist
        report = request.data['report']
        my_taking = get_object_or_404(Taking, pk=request.data.get('id_taking'))
        forced =  True if request.data.get('force') == 'True' else False
        team = get_object_or_404(Team, pk=request.data.get('id_team'))
        
        if not my_taking.is_active:
            return Response(
                {'message': "Inventario Cerrado"},
                status=400
            )
        
        # El forzado es para obligar el registro de los datos, pero si el token
        # no existe, se registra de forma normal aunque este forzado
        # sino se registran los datos de forzados anadiendo el texto 
        # *sycn forced!* al inicio de las notas
        if forced == True:
            if not TakinDetail.token_exist(request.data['token_team']):
                check_sum = self.register_taking(
                    report, my_taking, team, request.data['token_team']
                )

                return Response(check_sum, status=201)

            self.register_taking(
                report, my_taking, team, request.data['token_team'], force=True
            )

            return Response(
                {'message': "Datos sincronizados de forma Forzada"},
                status=201
        )
        
        if TakinDetail.token_exist(request.data['token_team']):
            return Response(
                {'message': "Datos ya registrados"},
                status=400
            )
        

        check_sum = self.register_taking(
            report, my_taking, team, request.data['token_team']
        )

        return Response(check_sum, status=201)

    def register_taking(self, report, my_taking, team, token_team, force=False):
        for item in report:
            product = Product.get_by_pk(item['id_product'])
            date_expiry = None
            if item['date_expiry']:
                date_expiry = date(
                    int(item['date_expiry'].split('-')[0]),
                    int(item['date_expiry'].split('-')[1]),
                    int(item['date_expiry'].split('-')[2])
                )
            notes = '*sycn forced!* ' + item['notes'] if force else item['notes']

            TakinDetail.objects.create(
                id_taking = my_taking,
                account_code = product,
                id_team = team,
                token_team = token_team,
                taking_total_boxes = item['taking_total_boxes'],
                taking_total_bottles = item['taking_total_bottles'],
                quantity=(
                    item["taking_total_boxes"] * product.quantity_per_box
                ) + item["taking_total_bottles"],
                notes = notes,
                year = int(item['year']) if item['year'] else None,
                date_expiry = date_expiry
            )
        
        return self.verify_sums(my_taking, team, token_team)

    def verify_sums(self, taking, team, token_team):
        sums = {
            'skus': 0,
            'quantity': 0,
            'taking_total_boxes': 0,
            'taking_total_bottles': 0,
        }

        details = TakinDetail.objects.filter(
            id_team=team,
            id_taking=taking,
            token_team=token_team
        )
        
        if not details:
            return sums

        for detail in details:
            sums['quantity'] += detail.quantity
            sums['taking_total_boxes'] += detail.taking_total_boxes
            sums['taking_total_bottles'] += detail.taking_total_bottles

        sums['skus'] = len(details)
        
        return sums
