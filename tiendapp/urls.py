from django.urls import path
from .views import v_index, v_cart, v_product_detail

urlpatterns = [
    path("", v_index, name="index"),
    path("cart", v_cart, name="cart"),
    path("product/<code>", v_product_detail, name="product_detail"),
]