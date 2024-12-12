from django.urls import path
from .views import v_index, v_cart, v_product_detail, v_add_to_cart

urlpatterns = [
    path("", v_index, name="index"),
    path("cart", v_cart, name="cart"),
    path("product/<code>", v_product_detail, name="product_detail"),
    path("add_to_cart/<code>", v_add_to_cart, name="add_to_cart"),
]