import json

from django.core.serializers import serialize
from django.views.generic import TemplateView

from common import loggin
from products.models import Product
from sap_migrations.models import SapMigration
from takings.models import TakinDetail
from warenhouses.models import Warenhouse


# /takings/<int:id_sap_migration>
class Taking(TemplateView):
	template_name = 'takings/taking-mobile.html'

	def get(self, request, id_taking, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		products = serialize('json', Product.objects.all())
		warenhouses = Warenhouse.objects.all()

		warenhouses = [ {'name': whrs.name, 'pk': whrs.pk} 
			for whrs in warenhouses 
		]

		page_data = {
			'title_page': 'Toma Inventario',
			'module_name': 'Toma',
			'products': products,
			'warenhouses': warenhouses,
			'id_taking': id_taking,
		}

		return self.render_to_response({**context, **page_data})

	def post(self, request, *args, **kwargs):
		pass