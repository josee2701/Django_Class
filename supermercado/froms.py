from django import forms

from .models import Product


class ProductoForm(forms.ModelForm):
    """Form definition for Producto."""

    class Meta:
        """Meta definition for Productoform."""

        model = Product
        fields = ('__all__')
