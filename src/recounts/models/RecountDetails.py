from django.db import models

from common import AppBaseModel
from recounts.models import RecountTakings
from products.models import Product
from accounts.models.Team import Team


class RecountDetails(AppBaseModel):
    id_recount_detail = models.AutoField(
        'id detalle reconteo',
        primary_key=True
    )
    id_recount_taking = models.ForeignKey(
        RecountTakings,
        on_delete=models.RESTRICT
    )
    account_code = models.ForeignKey(
        Product,
        on_delete=models.RESTRICT
    )
    taking_total_boxes = models.PositiveIntegerField(
        'conteo cajas',
        blank=True,
        null=True,
        default=0
    )
    taking_total_bottles = models.PositiveIntegerField(
        'conteo botellas',
        blank=True,
        null=True,
        default=0
    )
    quantity = models.PositiveIntegerField(
        'cantidad unidades',
        blank=True,
        null=True,
        default=0
    )
    detail = models.JSONField(
        'detalle completo',
        blank=True,
        null=True,
    )
