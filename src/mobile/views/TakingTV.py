import json

from django.core.serializers import serialize
from django.views.generic import TemplateView
from django.http import HttpResponseBadRequest

from products.models import Product
from sap_migrations.models import SapMigration, SapMigrationDetail
from accounts.models.Team import Team
from accounts.models.CustomUserModel import CustomUserModel
from accounts.mixins import ValidateAssistantMixin
from takings.models import TakinDetail, Taking


# /takings/<int:id_sap_migration>
class TakingTV(ValidateAssistantMixin, TemplateView):
    template_name = 'mobile/taking.html'

    def get(self, request, id_taking, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user = CustomUserModel.get(request.user)
        taking = Taking.get(id_taking)
        products = serialize('json', self.get_products(taking))
        my_team = None
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

    def get_products(self, taking):
        found_poducts = []
        products = json.loads(taking.id_sap_migration.report)['products']
        for account_code in products:
            obj_product = Product.get(account_code)
            if obj_product is None:
                new_product = SapMigrationDetail.objects.filter(account_code=account_code).first()
                my_product = Product.objects.create(
                    account_code=account_code,
                    name=new_product.name
                )
                raise Exception('El prodycto {} no existe en la base'.format(account_code))
            found_poducts.append(obj_product)

        return found_poducts

