# coprobamos los enlaces de las imagenes de los productos

from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help='Comprueba los enlaces de las imagenes de los productos'

    def handle(self, *args, **kwargs):
        queryset = Product.objects.all()
        errors = []

        print('Verificando urls de imagenes')
        for product in queryset:
            if product.image_front:
                if not product.image_front.url.startswith('/media/app/images/products/'):
                    print('Corrigiendo Url')
                    old_url = product.image_front.url.replace(
                        '/app/products/images/', '/app/images/products/'
                    ).split('/')
                    index = old_url.index('app')
                    product.image_front = '/'.join(old_url[index:])
                    product.save()
                    print('Url corregida {}'.format(product.name))

            else:
                errors.append(product)

        print('Productos sin imagen')
        for product in errors:
            print('{}->{}'.format(product.account_code, product.name))           
              
