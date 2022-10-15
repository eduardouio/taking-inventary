from django.db import models
from products.models import Product
from common import AppBaseModel
from crum import get_current_user
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
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user is None:
            return super(InitialStock, self).save(*args, **kwargs)

        if not self.pk:
            self.id_user_created = user.pk
        self.id_user_updated = user.pk
        
        return super(InitialStock, self).save(*args, **kwargs)

    def __str__(self):
        return '{}->{}'.format(
            self.id_product.name,
            self.id_product.quantity,
        )