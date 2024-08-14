from django.urls import path
from .views import ProductView

urlpatterns = [
    path('catalogo/', ProductView.as_view(), name='catalogo'),
]