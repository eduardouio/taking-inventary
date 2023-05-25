from django.db import models
from common import AppBaseModel
from takings.models import Taking
from products.models import Product


class TakingJustify(AppBaseModel):
    """
        Justifies a difference un report
    """
    id_taking_comment = models.AutoField(
        primary_key=True
    )
    id_taking = models.ForeignKey(
        Taking,
        on_delete=models.PROTECT
    )
    id_product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )
    justify = models.CharField(
        'justificacion',
        max_length=1200,
    )
    audit_comments = models.CharField(
        'Comentarios Auditoria',
        max_length=1200,
        blank=True,
        null=True,
        default=None
    )
    is_it_aproved = models.BooleanField(
        '¿Aprobado?',
        blank=True,
        null=True,
        default=False
    )

    class Meta:
        unique_together = ('id_taking', 'id_product')
