import json
from secrets import token_hex

from django.views import View
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin
from django.middleware.csrf import get_token
from accounts.models.CustomUserModel import CustomUserModel
from takings.models import Taking
from products.models import Product
from sap_migrations.models import SapMigrationDetail


# /takings/api/taking/<int:id_taking>/
class APITaking(View):

    def get(self, request, id_taking, *args, **kwargs):
        # user = CustomUserModel.get(request.user)
        user = CustomUserModel.get("evillota")
        taking = Taking.get(id_taking)
        products = serialize("json", self.get_products(taking))
        my_team = None
        for team in taking.teams.all():
            if team.manager == user:
                team.token_team = token_hex(32)
                team.save()
                my_team = team
                break

        if my_team is None:
            my_team = taking.teams.all()[0]  # for test
            my_team.token_team = token_hex(32)  # for test
            my_team.save()  # for test
            # raise Exception("Your team not in this taking")

        taking_data = {
            "taking": json.loads(serialize("json", [taking]))[0],
            "team": json.loads(serialize("json", [my_team]))[0],
            "products": json.loads(products),
            "user": json.loads(serialize("json", [user]))[0],
            "csrf_token": get_token(request),
        }
        del (taking_data["user"]["fields"]["password"])
        del (taking_data["user"]["fields"]["groups"])
        del (taking_data["user"]["fields"]["user_permissions"])

        return JsonResponse(taking_data)

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
