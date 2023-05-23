import simplejson as json
from ipdb import set_trace

from django.views.generic import View
from django.http import JsonResponse
from django.core.serializers import serialize

from takings.lib import ConsolidateTaking
# /api/takings-manager/<id_taking>/


class APITakingManager(View):

    def get(self, request, id_taking, *args, **kwargs):
        view_report = self.serialize_report(ConsolidateTaking().get(id_taking))
        view_data = {
            "report": view_report,
        }

        return JsonResponse(view_data, status=200, safe=False)

    def serialize_report(self, report):
        sales_report = []
        for item in report['report']:
            sales_report.append({
                "product": json.loads(serialize("json", [item["product"]]))[0],
                "sap_stock": item["sap_stock"],
                "sku_code": item["sku_code"] if "sku_code" in item else '',
                "is_complete": item["is_complete"] if "is_complete" in item else False,
                "diff": item["diff"],
                "quantity": item["tk_quantity"] if "tk_quantity" in item else 0,
                "taking_total_bottles": item['tk_bottles'] if "tk_bottles" in item else 0,
                "taking_toal_boxes": item["tk_boxes"] if "tk_boxes" in item else 0,
            })
        report['taking'] = json.loads(serialize("json", [report["taking"]]))[0]
        report['report'] = sales_report
        return report
