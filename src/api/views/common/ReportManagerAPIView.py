from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.db import connection


class ReportManagerAPIView(APIView):

    def get(self, *args, **kwargs):
        report = self.getQuery(kwargs['id_taking'])

        if not report:
            return Response({}, status=HTTP_400_BAD_REQUEST)
        
        if report:
            return Response(report, status=HTTP_200_OK)
        
        return Response({}, status=HTTP_400_BAD_REQUEST)

    def getQuery(self, id_taking):
        report = []
        query = """ 
            SELECT  
                pp.account_code,
                pp."name",
                tkd.year,
                pp.quantity_per_box,
                tkd.date_expiry,
                tkd.notes,
                au.username,
                tkd.taking_total_boxes,
                tkd.taking_total_bottles,
                tkd.quantity,
                CONCAT(au.first_name, ' ' , au.last_name) AS "user"
            FROM takings_takindetail tkd
            JOIN products_product pp on (pp.id_product = tkd.account_code_id)
            JOIN accounts_team tm on (tm.id_team = tkd.id_team_id)
            JOIN accounts_customusermodel au on (au.id = tm.manager_id)
            where id_taking_id = {}
            ORDER by pp."name";
        """.format(id_taking)

        with connection.cursor() as cursor:
            cursor.execute(query)
            report = cursor.fetchall()
        
        columns = [col[0] for col in cursor.description]
        report = [dict(zip(columns, row)) for row in report]
        return report