from django.views.generic import TemplateView


# /migraciones/todos/
class MigrationTV(TemplateView):
    template_name = 'base/base.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context=context)