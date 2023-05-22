from django.urls import path
from core.views import index, carrito

urlpatterns = [
    path('', index,name="index"),
    path("carrito", carrito, name="carrito")
]