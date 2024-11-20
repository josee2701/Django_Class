from django.urls import path

from .views import (AddProductos, AddStock, AddVenta, DeleteProductos,
                    IndexView, ListProductos, ListStock, ListVentas,
                    UpdateProductos)

# Define la lista de URL pattern
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("ventas/", ListVentas.as_view(), name="ventas"),
    path("ventas/addventas", AddVenta.as_view(), name="addventas"),
    path("stock/", ListStock.as_view(), name="stock"),
    path("stock/addstock", AddStock.as_view(), name="addstock"),
    path("productos/", ListProductos.as_view(), name="productos"),
    path("productos/addproductos/", AddProductos.as_view(), name="addProductos"),
    path("productos/updateproductos/<int:pk>/", UpdateProductos.as_view(), name="updateProductos"),
    path("productos/deleteproductos/<int:pk>/", DeleteProductos.as_view(), name="deleteProductos"),
]
