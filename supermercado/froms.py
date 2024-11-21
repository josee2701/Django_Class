from django import forms

from .models import Cliente, MetodoPago, Product, Stock, Venta


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
        
class CompraForm(forms.Form):
    # Campos relacionados con el cliente
    nombre_cliente = forms.CharField(max_length=255, label="Nombre del Cliente")
    direccion_cliente = forms.CharField(max_length=255, label="Dirección")
    telefono_cliente = forms.CharField(max_length=20, label="Teléfono")
    correo_cliente = forms.EmailField(label="Correo Electrónico")
    
    # Otros campos de la compra
    metodo_pago = forms.ModelChoiceField(queryset=MetodoPago.objects.all(), label="Método de Pago")
    producto_id = forms.IntegerField(widget=forms.HiddenInput())  # Producto seleccionado
    cantidad = forms.IntegerField(min_value=1, label="Cantidad")