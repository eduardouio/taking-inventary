from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from common import AppBaseModel

UNITS = (
    ('LITROS', 'LITROS'),
    ('MILITROS', 'MILILITROS'),
    ('GRAMOS', 'GRAMOS'),
    ('MILIGRAMOS', 'MILIGRAMOS'),
    ('OTRO', 'OTRO'),
)

TYPE_PRODUCT = (
    ('ACCESORIO', 'ACCESORIO'),
    ('AGUA TONICA', 'AGUA TÓNICA'),
    ('ALIMENTO', 'ALIMENTO'),
    ('BAJATIVO', 'BAJATIVO'),
    ('BEBIDAS AZUCARADAS', 'BEBIDAS AZUCARADAS'),
    ('CHAMPAGNE', 'CHAMPAGNE'),
    ('MUEBLE', 'MUEBLE'),
    ('PISCO', 'PISCO'),
    ('RON', 'RON'),
    ('SANGRIA', 'SANGRIA'),
    ('VINO BLANCO', 'VINO BLANCO'),
    ('VINO ESPUMOSO', 'VINO ESPUMOSO'),
    ('VINO TINTO', 'VINO TINTO'),
    ('WHISKY', 'WHISKY'),
    ('OTRO', 'OTRO BIEN'),
)


class Product(AppBaseModel):
    id_product = models.AutoField(
        'id producto',
        primary_key=True
    )
    account_code = models.CharField(
        'codigo contable',
        max_length=50,
        unique=True
    )
    name = models.CharField(
        'nombre producto',
        max_length=300,
    )
    type_product = models.CharField(
        'tipo',
        max_length=255,
        choices=TYPE_PRODUCT,
        blank=True,
        null=True,
        default='LICORES;VARIOS'
    )
    quantity_per_box = models.PositiveSmallIntegerField(
        'cantidad por caja',
        blank=True,
        null=True,
        default=1
    )
    capacity = models.PositiveIntegerField(
        'capacidad',
        null=True,
        blank=True,
        default=0,
    )
    unit_measurement = models.CharField(
        'unidad medida',
        choices=UNITS,
        max_length=40,
        null=True,
        blank=True,
        default='otro',
    )
    sale_unit_measurement = models.CharField(
        'unidad medida venta',
        max_length=40,
        null=True,
        blank=True,
        default='UNIDAD'
    )
    alcoholic_strength = models.PositiveSmallIntegerField(
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
    ean_14_code = models.CharField(
        'EAN 14',
        max_length=25,
        null=True,
        blank=True,
        default=0,
    )
    health_register = models.CharField(
        'registro sanitario',
        max_length=50,
        null=True,
        blank=True,
        default=None
    )
    image_front = models.ImageField(
        'imagen frontal',
        upload_to='app/images/products',
        blank=True,
        null=True,
        default=None
    )
    image_back = models.ImageField(
        'imagen posterior',
        upload_to='app/images/products',
        blank=True,
        null=True,
        default=None
    )
    max_stock = models.SmallIntegerField(
        'stock máximo',
        blank=True,
        null=True,
        default=None
    )
    min_stock = models.SmallIntegerField(
        'stock mínimo',
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

    @classmethod
    def get(cls, account_code):
        try:
            return cls.objects.get(account_code=account_code)
        except ObjectDoesNotExist as e:
            return None

    @classmethod
    def get_by_pk(cls, pk):
        try:
            return cls.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            return None

    def __str__(self):
        return self.name
