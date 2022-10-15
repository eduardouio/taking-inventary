from django.db import models
from products.models import Product
from common import AppBaseModel
from .Taking import Taking


class InitialStock(AppBaseModel):
    id_initial_stock = models.AutoField(
        'id stock',
        primary_key=True
    )
    id_taking = models.ForeignKey(
        Taking,
        on_delete=models.RESTRICT
    )
    id_product = models.ForeignKey(
        Product, 
        on_delete=models.RESTRICT
        )
    quantity = models.PositiveSmallIntegerField(
        'cantidad',
        blank=True,
        null=True,
        default=0
    )
    is_complete = models.BooleanField(
        'esta completo',
        default=False
    )

    def __str__(self):
        return '{}->{}'.format(
            self.id_product.name,
            self.id_product.quantity,
        )