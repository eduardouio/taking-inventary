from unittest.util import _MAX_LENGTH
from simple_history.models import HistoricalRecords
from django.db import models
from common import AppBaseModel
from crum import get_current_user


DEALERS = (
    ('Agencias y Representaciones Cordovez', '1790023516001'),
    ('Imnac Importadora Nacional', '1791771907001'),
    ('Vidinternacional', '1791771907001'),
    ('Otros', '9999999999999'),
)

UNITS=(
    ('MM', 'Mililitros'),
    ('GR', 'Gramos'),
)


class Product(AppBaseModel):
    id_product=models.AutoField(
        'id producto',
        primary_key=True
    )
    cod_contable=models.CharField(
        'codigo contable',
        max_length=20,
        unique=True
    )
    name=models.CharField(
        'nombre producto',
        max_length=300,
        unique=True
    )
    quantity_per_box=models.PositiveSmallIntegerField(
        'cantidad por caja',
    )
    capacity=models.PositiveIntegerField(
        'capacidad',
        null=True,
        blank=True,
        default=0,
    )
    unit_measurement=models.CharField(
        'unidad_medida',
        choices=UNITS,
        max_length=40,
        null=True,
        blank=True,
        default='No Especidficado',
    )
    alcoholic_strength=models.PositiveSmallIntegerField(
        'grado alcoholico',
        default=None,
        blank=True,
        null=True,
    )
    ean_13_code = models.CharField(
        'EAN 13',
        max_length=25,
        null=True,
        blank=True,
    )
    ean_14_code=models.CharField(
        'EAN 14',
        max_length=25,
        null=True,
        blank=True,
        default=0,
    )
    manufactured_date = models.DateField(
        'fecha de elaboracion',
        blank=True,
        null=True,
        default=None
    )
    expiration_date = models.DateField(
        'feccha vencimiento',
        blank=True,
        null=True,
        default=None
    )
    health_register=models.CharField(
        'registro sanitario',
        max_length=50,
        null=True,
        blank=True,
        default=None
    )
    location=models.CharField(
        'ubicacion_producto',
        max_length=200,
        null=True,
        blank=True,
        default=None
    )
    manufacturer_name = models.CharField(
        'nombre fabricante',
        max_length=300,
        null=True,
        blank=True,
        default=None
    )
    dealer_name = models.CharField(
        'Nombre Importador',
        max_length=100,
        choices=DEALERS,
        default=None,
        blank=True,
        null=True
    )
    image_front=models.ImageField(
        'imagen frontal',
        upload_to='media/app/images/products',
        blank=True,
        null=True,
        default=None
    )
    image_back=models.ImageField(
        'imagen posterior',
        upload_to='media/app/images/products',
        blank=True,
        null=True,
        default=None
    )
    box_dimensions = models.CharField(
        'dimensiones caja madre',
        max_length=50,
        blank=True,
        null=True,
        default=None
    )
    product_dimensions = models.CharField(
        'dimensiones producto',
        max_length=50,
        blank=True,
        null=True,
        default=None
    )
    ice_code = models.CharField(
        'codigo ice',
        max_length=255,
        blank=True,
        null=True
    )
    history = HistoricalRecords()
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user is None:
            return super(Product, self).save(*args, **kwargs)
        
        if not self.pk:
            self.id_user_created = user.pk
        self.id_user_updated = user.pk
        return super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
