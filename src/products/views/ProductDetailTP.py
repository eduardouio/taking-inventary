from django.views.generic import TemplateView


# /product/detail/<ok>/
class ProductDetailTP(TemplateView):
    template_name = 'products/item_detail.html'

    def get(self, request, pk, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        page_data = {
            'title_page': 'Ficha de Producto',
        }
        return self.render_to_response({**context, **page_data})