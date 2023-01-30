from time import time

from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Product


# /products/<int:pk>/
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/item-detail.html'

    def get(self, request, pk, *args, **kwargs):
        start_time = time()
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        extra_fields = {
            'total_time': start_time - time(),
            'title_page': 'Detalle Producto',
            'was_created': False,
            'was_updated': False,
        }
        return self.render_to_response({**context, **extra_fields})
