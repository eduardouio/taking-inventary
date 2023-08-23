# coprobamos los enlaces de las imagenes de los productos

from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help='Comprueba los enlaces de las imagenes de los productos'

    def handle(self, *args, **kwargs):
        queryset = Product.objects.all()
        errors = []
    
        for product in queryset:
            if product.image_front:
                if not product.image_front.url.startswith('/media/app/products/images/'):
                    errors.append(product.account_code)
                    print('Producto:{} -> {} no tiene imagen {} '.format(
                        product.account_code,
                        product.name, product.image_front.url
                    ))
        
                if not product.image_front.url.endswith('.jpg'):
                    errors.append(product.account_code)
                    print('Producto:{} -> {} no tiene imagen {} '.format(
                        product.account_code,
                        product.name, product.image_front.url
                    ))
            else:
                print(product.account_code)
        self.stdout.write(
                self.style.SUCCESS('Terminamos la revision')
            )
              
