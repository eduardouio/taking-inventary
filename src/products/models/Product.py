from django.db import models
from common import AppBaseModel

UNITS=(
    ('MM', 'Mililitros'),
    ('GR', 'Gramos'),
    ('Otro', 'Otro'),
)

TYPE_PRODUCT = (
    ('alimento','Alimento'),
    ('vino','Vino'),
    ('espirituoso','Bebida Espirituoso'),
    ('mueble','Bien Mueble'),
    ('no_peresible','No Peresible'),
    ('accesorio','Accesorio'),
    ('mueble','Bien Mueble'),
    ('otro','Otro Bien'),
)


class Product(AppBaseModel):
    id_product=models.AutoField(
        'id producto',
        primary_key=True
    )
    account_code=models.CharField(
        'codigo contable',
        max_length=20,
        unique=True
    )
    name=models.CharField(
        'nombre producto',
        max_length=300,
        unique=True
    )
    type_product = models.CharField(
        max_length=255,
        choices=TYPE_PRODUCT,
        blank=True,
        null=True,
        default='otro'
    )
    quantity_per_box=models.PositiveSmallIntegerField(
        'cantidad por caja',
        blank=True,
        null=True,
        default=1
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
    sale_unit_measurement = models.CharField(
        'unidad_medida_venta',
        max_length=40,
        null=True,
        blank=True,
        default='UNIDAD'
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
        null=True,
        default=None
    )
    
    def __str__(self):
        return self.name
