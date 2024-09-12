from django.views import View
from django.views.generic import DetailView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from products.models import Product
from .models import Order, OrderProduct

# Create your views here.
class OrderView(LoginRequiredMixin ,DetailView):
    model = Order
    template_name = 'orders/order.html'
    context_object_name = 'order'

    # se replantea la funcion de get_object
        # hace que el usuario solo pueda ver su orden activa
    def get_object(self, queryset=None):
        return Order.objects.filter(user=self.request.user, is_active=True).first()
    
class AddOrderProductView(LoginRequiredMixin, View):
    def post(self, request, id_catalog):
        product = get_object_or_404(Product, id_catalog=id_catalog)
        order, _ = Order.objects.get_or_create(user = request.user)
        order_product, created = OrderProduct.objects.get_or_create(order=order, product=product)

        if not created:
            order_product.quantity += 1
            order_product.save()

        return HttpResponse(status=204)

