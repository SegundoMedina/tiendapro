from django.urls import path
from .views import v_index, v_cart

urlpatterns = [
    path("", v_index, name="index"),
    path("cart", v_cart, name="cart"),
]