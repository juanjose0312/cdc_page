from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    readonly_fields = ('name','available')
    list_display = ('id_catalog','name','cantidad','image','retail_price','wholesale_price')

admin.site.register(Product, ProductAdmin)