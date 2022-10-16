from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    search_fields= [
        'name',
        'account_code',
        'ean_13_code',
        'ean_14_code'
    ]
    
    fieldsets = (
        ('Información Básica',{
            'fields':(
                'account_code',
                'name',
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
                'health_register',
                'location',
                'image_front',
                'image_back',
                'notes',
            )
        }),
    )
    

admin.site.register(Product, ProductAdmin)
