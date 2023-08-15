from rest_framework.generics import DestroyAPIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from takings.models import TakinDetail
from rest_framework.response import Response


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
        if self.check_if_taking_is_open(kwargs['id_taking_detail']):
            return self.destroy(requests, *args, **kwargs)
        
        return Response({"status":"Toma Cerrada"},status=HTTP_400_BAD_REQUEST)

    def check_if_taking_is_open(self, id_taking_detail):
        detail = TakinDetail.get(id_taking_detail)
        if detail is None:
            return False
        
        if detail.id_taking.is_active:
            return True
        
        return False
