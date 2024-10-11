# Register your models here.
from django.contrib import admin

from .models import (CategoriaProducto, Cliente, MetodoPago, Product,
                     ProductoVenta, Stock, Venta)


class ProductoVentaInline(admin.TabularInline):
    """
    Permite añadir productos a la venta desde la vista de Venta.
    """
    model = ProductoVenta
    extra = 1  # Número de formularios adicionales para añadir nuevos productos en la vista de ventas


class VentaAdmin(admin.ModelAdmin):
    """
    Personaliza el modelo de Venta en el admin.
    """
    list_display = ('id', 'cliente', 'fecha', 'total', 'metodo_pago')
    inlines = [ProductoVentaInline]  # Permite añadir productos dentro de la venta
    readonly_fields = ('total',)

    def total(self, obj):
        """
        Calcula el total de la venta para mostrarlo en la vista del admin.
        """
        return obj.total


class ProductAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo Product.
    """
    list_display = ('nombre', 'precio', 'color')


class ClienteAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo Cliente.
    """
    list_display = ('nombre', 'telefono', 'correo', 'direccion')


class StockAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo Stock.
    """
    list_display = ('producto', 'cantidad', 'fecha')


class ProductoVentaAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo ProductoVenta.
    """
    list_display = ('venta', 'producto', 'cantidad', 'precio_unitario')


class MetodoPagoAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo MetodoPago.
    """
    list_display = ('tipo',)

class CategoriaProductoAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo CategoriaProducto.
    """
    list_display = ('nombre',)



# Registro de los modelos en el panel de administración
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(MetodoPago, MetodoPagoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(ProductoVenta, ProductoVentaAdmin)
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)

