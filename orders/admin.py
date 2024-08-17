from django.contrib import admin
from .models import Order, OrderProduct

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    model = Order
    #readonly_fields = ('user','is_active','order_date')
    #list_display = ('id','user','is_active','order_date')
    #search_fields = ('user','id')

admin.site.register(Order, OrderAdmin)