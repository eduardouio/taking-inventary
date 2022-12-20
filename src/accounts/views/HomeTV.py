from django.views.generic import TemplateView
from products.models import Product
from takings.models import Taking
from sap_migrations.models import SapMigration
from accounts.models.CustomUserModel import CustomUserModel
from accounts.mixins import ValidateManagerMixin


# /
class HomeTV(ValidateManagerMixin, TemplateView):
    template_name = 'accounts/home.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        total_sap_migrations = SapMigration.objects.all().count()
        total_users = CustomUserModel.objects.all().count()
        total_takings = Taking.objects.all().count()
        total_productos = Product.objects.all().count()

        page_data = {
            'tittle_page': 'Toma Inventarios',
            'total_sap_migrations': total_sap_migrations,
            'total_users': total_users,
            'total_takings': total_takings,
            'total_products': total_productos,
        }
        return self.render_to_response({**context, ** page_data})