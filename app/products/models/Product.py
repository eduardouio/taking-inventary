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
        'id_producto',
        primary_key=True
    )
    cod_contable=models.CharField(
        'codigo_contable',
        max_length=20,
        unique=True
    )
    name=models.CharField(
        'nombre_producto',
        max_length=300
    )
    quantity_per_box=models.PositiveSmallIntegerField(
        'cantidad_por_caja',
    )
    capacity=models.PositiveIntegerField(
        'capacidad',
    )
    unit_measurement=models.CharField(
        'unidad_medida',
        choices=UNITS,
    )
    alcoholic_strength=models.PositiveSmallIntegerField(
        'grado_alcoholico',
    )
    name_sap_erp = models.CharField(
        'nombre_producto',
        max_length=300
    )
    ean_13_code = models.CharField(
        'codigo_ean_13',
        max_length=25
    )
    ean_14_code=models.CharField(
        'codigo_ean_14',
        max_length=25
    )
    health_register=models.CharField(
        'registro_sanitario',
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
        max_length=300,
        null=True,
        blank=True,
        default=None
    )
    dealer_name = models.CharField(
        'nombre_proveedor_inicial',
        max_length=100,
        choices=DEALERS
    )
    image_front=models.ImageField(
        'imagen_frontal',
        upload_to='media/app/images/products',
        blank=True,
        null=True,
        default=None
    )
    image_back=models.ImageField(
        'imagen_posterior',
        upload_to='media/app/images/products',
        blank=True,
        null=True,
        default=None
    )
    
