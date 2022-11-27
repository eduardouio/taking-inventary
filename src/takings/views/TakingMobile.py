from django.views.generic import TemplateView
from django.core.serializers import serialize

from common import loggin
from products.models import Product
from sap_migrations.models import SapMigration


# /takings/<int:id_sap_migration>
class TakingMobile(TemplateView):
	template_name = 'takings/taking-mobile.html'

	def get(self, request, id_sap_migration, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		all_products = Product.objects.all()
		sap_migration = SapMigration.get(id_sap_migration)
		sap_migration_json = serialize('json', [sap_migration])
		page_data = {
			'title_page': 'Toma Inventario',
			'module_name': 'Toma',
			'all_products': serialize('json', all_products),
			'sap_migration': sap_migration,
			'sap_migration_json': sap_migration_json[0],
		}

		return self.render_to_response({**context, **page_data})

