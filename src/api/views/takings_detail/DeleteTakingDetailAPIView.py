from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from takings.models import TakinDetail


# /api/takings-detail/delete/<int:id_taking_detail>/
class DeleteTakingDetailAPIView(DestroyAPIView):
    """ 
        Elimina una toma de inventario
    """
    queryset = TakinDetail.objects.all()
    lookup_field = 'id_taking_detail'

    def delete(self, requests, *args, **kwargs):
        """
        Maneja la solicitud de eliminación de un objeto TakingDetail.
        Elimina el objeto y devuelve una respuesta exitosa sin contenido.
        """
        return self.destroy(requests, *args, **kwargs)
