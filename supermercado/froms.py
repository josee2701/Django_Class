from django import forms

from .models import Product, Stock, Venta


class ProductoForm(forms.ModelForm):
    """Form definition for Producto."""

    class Meta:
        """Meta definition for Productoform."""

        model = Product
        fields = ('__all__')

class StockForm(forms.ModelForm):
    """Form definition for Producto."""

    class Meta:
        """Meta definition for Productoform."""

        model = Stock
        fields = ('__all__')

class VentaForm(forms.ModelForm):
    """Form definition for Producto."""

    class Meta:
        """Meta definition for Productoform."""

        model = Venta
        fields = ('__all__')

