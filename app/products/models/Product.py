from simple_history.models import HistoricalRecords
from django.db import models
from common import AppBaseModel


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
    )
    unit_measurement=models.CharField(
        'unidad_medida',
        choices=UNITS,
        max_length=40,
    )
    alcoholic_strength=models.PositiveSmallIntegerField(
        'grado alcoholico',
        default=None,
        blank=True,
        null=True
    )
    ean_13_code = models.CharField(
        'EAN 13',
        max_length=25
    )
    ean_14_code=models.CharField(
        'EAN 14',
        max_length=25
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
    ice_code = models.CharField(
        'codigo ice',
        max_length=255,
        blank=True,
        null=True
        )
    history = HistoricalRecords()
