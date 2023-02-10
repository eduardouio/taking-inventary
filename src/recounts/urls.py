from django.urls import path
from recounts.views import MakeRecountView

app_name = 'recounts'

urlpatterns = [
    path('make/taking/<int:id_taking>/product/<str:account_code>',
         MakeRecountView.as_view(), name='make-recount'),
]
