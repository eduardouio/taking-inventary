from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    search_fields= [
        'name',
        'account_code',
        'ean_13_code',
        'ean_14_code'
    ]
    
    list_display= [
        'pk',
        'name',
        'type_product',
        'capacity',
        'quantity_per_box',
        'unit_measurement',
        'sale_unit_measurement',
        'health_register',
        'location',
    ]
    
    

    fieldsets = (
        ('Información Básica',{
            'fields':(
                'account_code',
                'name',
                'type_product',
                'capacity',
                'unit_measurement',
                'quantity_per_box',
                'ean_13_code',
                'ean_14_code',
            )
        }),
        ('Datos Adicionales',{
            'fields':(
                'alcoholic_strength',
                'sale_unit_measurement',
                'health_register',
                'location',
                'image_front',
                'image_back',
                'box_dimensions',
                'product_dimensions',
                'ice_code',
                'notes',
            )
        }),
    )
    

admin.site.register(Product, ProductAdmin)
