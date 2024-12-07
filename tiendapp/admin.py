from django.contrib import admin
from tiendapp.models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
