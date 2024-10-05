from django.urls import path

from .views import IndexView, ListProductos, ListStock, ListVentas

# Define la lista de URL pattern
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("ventas/", ListVentas.as_view(), name="ventas"),
    path("stock/", ListStock.as_view(), name="stock"),
    path("productos/", ListProductos.as_view(), name="productos"),
]
