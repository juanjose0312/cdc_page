from django.views.generic import ListView
from .models import Product

# Create your views here.
class ProductView(ListView):
    model = Product
    template_name = 'products/list_products.html'
    context_object_name = 'products'
    #queryset = Product.objects.all()
