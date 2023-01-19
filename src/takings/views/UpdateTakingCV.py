import json

from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from takings.models import Taking, TakinDetail
from accounts.models.Team import Team
from products.models import Product


# /takings/add/report/
class UpdateTakingCV(LoginRequiredMixin, CreateView):
    def post(self, request, *args, **kwargs):
        report_data = json.loads(request.POST.get('report'))
        if not report_data:
            return HttpResponse('Missing report data', status=400)
        
        id_taking = json.loads(request.POST.get('taking'))
        if not id_taking:
            return HttpResponse('Missing taking data', status=400)

        team_data = json.loads(request.POST.get('team'))
        if not team_data:
            return HttpResponse('Missing team data', status=400)

        try:
            team = Team.objects.get(id_team=team_data['pk'])
            taking = Taking.get(id_taking=id_taking)
            report = []

            for item in report_data:
                product = Product.objects.get(account_code=item['product']['fields']['account_code'])
                
                my_taking = TakinDetail(
                    id_taking=taking,
                    account_code=product,
                    id_team=team,
                    taking_total_boxes=item['taking_total_boxes'],
                    taking_total_bottles=item['taking_total_bottles'],
                    quantity = (item['taking_total_boxes'] * product.quantity_per_box) + item['taking_total_bottles'],
                    notes=item['notes']
                )
                report.append(my_taking)
            
            TakinDetail.objects.bulk_create(report)
            
            return HttpResponse('Updated success', status=201)
        
        except Team.DoesNotExist:
            return HttpResponse('Team not found', status=404)
        except Taking.DoesNotExist:
            return HttpResponse('Taking not found', status=404)
        except Product.DoesNotExist:
            return HttpResponse('Product not found', status=404)
        except Exception as e:
            return HttpResponse(str(e), status=500)