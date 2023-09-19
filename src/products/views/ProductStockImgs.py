from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from sap_migrations.lib import ConsolidateMigration
from sap_migrations.models import SapMigration

from products.models import Product

# /products/list-imgs/
class ProductStockImgs(LoginRequiredMixin, ListView):
    template_name = 'products/stock-imgs.html'

    def get_queryset(self):
        migration = SapMigration.objects.filter().order_by(
            '-id_sap_migration'
        ).first()
        consolidate = ConsolidateMigration().get(migration.pk)
        skus = [x for x in consolidate['products']]
        products = Product.objects.filter(account_code__in=skus)
        return products
