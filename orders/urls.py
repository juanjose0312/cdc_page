from django.urls import path
from .views import OrderView, AddOrderProductView

urlpatterns = [
    path('orden/', OrderView.as_view(), name='orden'),
    path('agregar_producto/<str:id_catalog>/', AddOrderProductView.as_view(), name='agregar_producto'),
]