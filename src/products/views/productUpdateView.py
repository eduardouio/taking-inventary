import json

from django.http import HttpResponse
from products.models import Product


def updateProduct(request):
    if request.method == 'GET':
        return HttpResponse('only post request', status='200')

    request_data = json.loads(request.POST.get('product'))
    new_product = request_data['fields']
    old_product = Product.objects.get(pk=request_data['pk'])
    old_product.box_dimensions = new_product['box_dimensions'].upper() if new_product['box_dimensions'] else None
    old_product.product_dimensions = new_product['product_dimensions'].upper() if new_product['product_dimensions'] else None
    old_product.type_product = new_product['type_product'].upper() if new_product['type_product'] else None
    old_product.notes = new_product['notes'].upper() if new_product['notes'] else None
    old_product.save()
    return HttpResponse('updated success', status='201')
