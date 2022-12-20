import json

from django.core.serializers import serialize
from django.views.generic import TemplateView

from products.models import Product
from sap_migrations.models import SapMigration
from accounts.models.Team import Team
from accounts.models.CustomUserModel import CustomUserModel
from accounts.mixins import ValidateAssistantMixin
from takings.models import TakinDetail, Taking
from warenhouses.models import Warenhouse


# /takings/<int:id_sap_migration>
class TakingTV(ValidateAssistantMixin, TemplateView):
	template_name = 'mobile/taking.html'

	def get(self, request, id_taking, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		user = CustomUserModel.get(request.user)
		products = serialize('json', Product.objects.all())
		warenhouses = Warenhouse.objects.all()
		warenhouses = [ {'name': whrs.name, 'pk': whrs.pk} 
			for whrs in warenhouses 
		]
		my_team = None
		taking = Taking.get(id_taking)
		for team in taking.teams.all():
			if team.manager == user:
				my_team = team
		if my_team is None:
			raise Exception('El ususario no se encuentra en la toma')
		my_team = serialize('json', [my_team])

		page_data = {
			'title_page': 'Toma Inventario',
			'module_name': 'Toma',
			'products': products,
			'taking': taking,
			'team': json.dumps(json.loads(my_team)[0]),
		}

		return self.render_to_response({**context, **page_data})
