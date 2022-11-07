from accounts.models import Team
from common import AppBaseModel, loggin
from django.db import models
from products.models import Product

from .Taking import Taking


class TakinDetail(AppBaseModel):
    id_taking_detail = models.AutoField(
        'id stock',
        primary_key=True
    )
    id_taking = models.ForeignKey(
        Taking,
        on_delete=models.RESTRICT
    )
    account_code = models.ForeignKey(
        Product, 
        on_delete=models.RESTRICT
    )
    id_team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT
    )
    quantity = models.PositiveSmallIntegerField(
        'cantidad unidades',
        blank=True,
        null=True,
        default=0
    )
    location = models.CharField(
        'ubicacion en bodega',
        max_length=255,
        blank=True,
        null=True,
        default=None
    )
    id_warenhouse_sap_code = models.CharField(
        'identificador_sap',
        max_length=10,
        blank=True,
        null=True,
        default=None
    )
    date_make = models.DateField(
        'fecha elaboracion',
        blank=True,
        null=True,
        default=None,
    )
    date_expiry = models.DateField(
        'fecha vencimiento',
        blank=True,
        null=True,
        default=None,
    )
    year = models.SmallIntegerField(
        'añana del vino',
        blank=True,
        null=True,
        default=None
    )
    is_complete = models.BooleanField(
        'esta completo?',
        default=False
    )
    
    @classmethod
    def get_by_taking(cls, id_taking):
        detail = cls.objects.filter(id_taking=id_taking)
        if len(detail):
            return list(detail)
        loggin('w')
        return []

    def __str__(self):
        return '{}->{}'.format(
            self.account_code,
            self.quantity,
        )
