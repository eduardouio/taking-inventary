import json

from django.core.serializers import serialize
from django.views.generic import TemplateView
from django.http import HttpResponseBadRequest

from products.models import Product
from sap_migrations.models import SapMigration
from accounts.models.Team import Team
from accounts.models.CustomUserModel import CustomUserModel
from accounts.mixins import ValidateAssistantMixin
from takings.models import TakinDetail, Taking
from warenhouses.models import Warenhouse


# /takings/<int:id_sap_migration>
class TakingTV(ValidateAssistantMixin, TemplateView):
    template_name = 'mobile/taking.html'

    def get(self, request, id_taking, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user = CustomUserModel.get(request.user)
        products = serialize('json', Product.objects.all())
        warenhouses = Warenhouse.objects.all()
        warenhouses = [ {'name': whrs.name, 'pk': whrs.pk} 
            for whrs in warenhouses 
        ]
        my_team = None
        taking = Taking.get(id_taking)
        for team in taking.teams.all():
            if team.manager == user:
                my_team = team
        if my_team is None:
            raise Exception('El ususario no se encuentra en la toma')
        my_team = serialize('json', [my_team])
        taking = serialize('json', [taking])
        user = serialize('json', [request.user])
        user = json.loads(user)[0]
        del(user['fields']['password'])

        page_data = {
            'title_page': 'Toma Inventario',
            'module_name': 'Toma',
            'products': products,
            'taking': json.dumps(json.loads(taking)[0]),
            'team': json.dumps(json.loads(my_team)[0]),
            'user': json.dumps(user),
        }

        return self.render_to_response({**context, **page_data})

    def post(self, request, id_taking, *args, **kwargs):
        taking_report = json.loads(request.POST.get('report'))
        if not taking_report:
            return HttpResponseBadRequest(
                'request data is null, please try later'
            )
            
        

        import ipdb;ipdb.set_trace()