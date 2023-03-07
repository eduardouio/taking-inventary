import json
from secrets import token_hex

from django.core.serializers import serialize
from django.views.generic import TemplateView

from products.models import Product
from sap_migrations.models import SapMigrationDetail, SapMigration
from accounts.models.CustomUserModel import CustomUserModel
from accounts.mixins import ValidateAssistantMixin
from takings.models import Taking


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
                team.token_team = token_hex(32)
                team.save()
                my_team = team

        if my_team is None:
            raise Exception('El ususario no se encuentra en la toma')
        my_team = serialize('json', [my_team])
        taking = serialize('json', [taking])
        user = serialize('json', [request.user])
        user = json.loads(user)[0]
        del (user['fields']['password'])

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
        products = []
        warenhouses = json.loads(taking.warenhouses)

        for warenhouse in warenhouses:
            result = list(SapMigrationDetail.objects.filter(
                warenhouse_name=warenhouse,
                id_sap_migration=taking.id_sap_migration
            ))

            if result:
                products = products + result

        uniques_products = list(set([x.account_code for x in products]))
        founded_products = []

        for account_code in uniques_products:
            obj_product = Product.get(account_code)
            if obj_product is None:
                new_product = SapMigrationDetail.objects.filter(
                    account_code=account_code
                ).first()
                obj_product = Product.objects.create(
                    account_code=account_code,
                    name=new_product.name,
                    quantity_per_box=new_product.quantity_per_box,
                    ean_13_code=new_product.ean_13_code,
                    health_register=new_product.health_register,
                )

            founded_products.append(obj_product)

        return founded_products
