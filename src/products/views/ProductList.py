from time import time

from django.views.generic import ListView
from products.models import Product


# /products/
class ProductList(ListView):
    template_name = 'products/product-list.html'
    model = Product

    def get(self, request, *args, **kwargs):
        start_time = time()
        self.object_list = self.get_queryset(**kwargs)
        context = self.get_context_data(**kwargs)

        extra_fields = {
            'title_page': 'Listado Productos',
            'module_name': 'Productos',
            'total_records': len(self.object_list),
            'total_time': time() - start_time,
            'last_product': self.object_list.first(),
        }

        return self.render_to_response({**context, **extra_fields})
