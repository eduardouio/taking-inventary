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
                if not product.image_front.url.startswith('/media/app/images/products/'):
                    import ipdb; ipdb.set_trace()
                    errors.append(product.account_code)
                    print('Corrigiendo Url')
                    print(product.image_front.url)
                    print(product.image_front.url.replace(
                        '/app/products/images/', '/app/images/products/'
                    ))
                    product.image_front = product.image_front.url.replace(
                        '/app/products/images/', '/app/images/products/'
                    ).split('/')[:]
                    product.save()
                    print('Url corregida')
                    print('Producto:{} -> {} no tiene imagen {} '.format(
                        product.account_code,
                        product.name, product.image_front.url
                    ))
               

            #else:
            #    self.stdout.write(
            #        self.style.ERROR('El producto {} -> {} no tiene imagen'.format(
            #            product.account_code, product.name
            #        ))
            #    )    
        self.stdout.write(
                self.style.SUCCESS('Terminamos la revision')
            )
              
