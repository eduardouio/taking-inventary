from django.db import models
from common import AppBaseModel
from takings.models import Taking
from products.models import Product


class TakingJustify(AppBaseModel):
    """
        Justifies a difference un report
    """
    id_taking_comment = models.IntegerField(
        primary_key=True
    )
    id_taking = models.ForeignKey(
        Taking
    )
    id_product = models.ForeignKey(
        Product
    )
    justify = models.CharField(
        'justificacion',
    )
    audit_comments = models.CharField(
        'Comentarios Auditoria',
        blank=True,
        null=True,
        default=None
    )
    is_it_aprobate = models.BooleanField(
        '¿Aprobado?',
        blank=True,
        null=True,
        default=False
    )

    class Meta:
        unique_together = ('id_taking', 'id_product')
