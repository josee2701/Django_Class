from django.urls import path

from .views import (AddProductos, AddStock, AddVenta, ComprarProductoView,
                    DeleteProductos, DeleteStock, IndexView, ListProductos,
                    ListStock, ListVentas, UpdateProductos, UpdateStock)

# Define la lista de URL pattern
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("compras/<int:producto_id>/", ComprarProductoView.as_view(), name="compras"),
    path("ventas/", ListVentas.as_view(), name="ventas"),
    path("ventas/addventas", AddVenta.as_view(), name="addventas"),
    path("stock/", ListStock.as_view(), name="stock"),
    path("stock/addstock", AddStock.as_view(), name="addstock"),
    path("stock/updatestock/<int:pk>/", UpdateStock.as_view(), name="updateStock"),
    path("stock/deletestock/<int:pk>/", DeleteStock.as_view(), name="deleteStock"),
    path("productos/", ListProductos.as_view(), name="productos"),
    path("productos/addproductos/", AddProductos.as_view(), name="addProductos"),
    path("productos/updateproductos/<int:pk>/", UpdateProductos.as_view(), name="updateProductos"),
    path("productos/deleteproductos/<int:pk>/", DeleteProductos.as_view(), name="deleteProductos"),
]
