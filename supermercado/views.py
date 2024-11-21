from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, FormView, ListView,
                                  TemplateView, UpdateView)

from.models import Cliente, Product, ProductoVenta,Stock,Venta
from django.contrib import messages
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .froms import CompraForm, ProductoForm, StockForm, VentaForm
from .models import Product, ProductoVenta, Stock, Venta

# Create your views here.

class IndexView(TemplateView):
    template_name= 'index.html'
    
    def get_context_data(self, **kwargs):
        # Llama al método base para obtener el contexto inicial
        context = super().get_context_data(**kwargs)

        # Filtra productos que tengan al menos 1 unidad en stock
        productos_en_stock = Product.objects.filter(stock__cantidad__gt=0).distinct()

        # Agrega los productos al contexto
        context['productos_en_stock'] = productos_en_stock
        return context
class ComprarProductoView(View):
    template_name = 'cliente/add_compra.html'

    def get(self, request, *args, **kwargs):
        producto_id = kwargs.get('producto_id')  # Obtener el ID del producto desde la URL
        producto = get_object_or_404(Product, id=producto_id)
        form = CompraForm(initial={'producto_id': producto.id})
        return render(request, self.template_name, {'form': form, 'producto': producto})

    def post(self, request, *args, **kwargs):
        form = CompraForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre_cliente']
            direccion = form.cleaned_data['direccion_cliente']
            telefono = form.cleaned_data['telefono_cliente']
            correo = form.cleaned_data['correo_cliente']
            cliente = Cliente.objects.create(
                nombre=nombre,
                direccion=direccion,
                telefono=telefono,
                correo=correo,
            )
            # Recuperar datos del formulario
            metodo_pago = form.cleaned_data['metodo_pago']
            producto_id = form.cleaned_data['producto_id']
            cantidad = form.cleaned_data['cantidad']

            # Validar existencia de stock
            producto = get_object_or_404(Product, id=producto_id)
            stock = Stock.objects.filter(producto=producto).first()
            if not stock or stock.cantidad < cantidad:
                messages.error(request, 'Stock insuficiente para realizar la compra.')
                return redirect('comprar_producto', producto_id=producto.id)

            # Crear la venta
            venta = Venta.objects.create(cliente=cliente, metodo_pago=metodo_pago)

            # Registrar el producto en la venta
            ProductoVenta.objects.create(
                venta=venta,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=producto.precio,
            )

            # Actualizar el stock
            stock.cantidad -= cantidad
            stock.save()

            messages.success(request, f'Compra realizada con éxito. Total: {venta.total}')
            return redirect('index')

        return render(request, self.template_name, {'form': form})
class ListProductos(ListView):
    template_name='productos/main_productos.html'
    model= Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class AddProductos(CreateView):
    template_name='productos/add_productos.html'
    model= Product
    form_class= ProductoForm

    def get_success_url(self):
        """
        Devuelve la URL de éxito a la que se redirige después de una creación exitosa.

        Returns:
            str: La URL de redirección.
        """
        return reverse("productos") 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def form_valid(self, form):
        # Guardamos el formulario para crear el objeto
        self.object = form.save()
        # Prepara una respuesta con redirección usando HTMX
        page_update = HttpResponse("")
        page_update["HX-Redirect"] = self.get_success_url()
        return page_update
    
class UpdateProductos(UpdateView):
    template_name='productos/update_productos.html'
    model= Product
    form_class= ProductoForm

    def get_success_url(self):
        """
        Devuelve la URL de éxito a la que se redirige después de una creación exitosa.

        Returns:
            str: La URL de redirección.
        """
        return reverse("productos") 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def form_valid(self, form):
        # Guardamos el formulario para crear el objeto
        self.object = form.save()
        # Prepara una respuesta con redirección usando HTMX
        page_update = HttpResponse("")
        page_update["HX-Redirect"] = self.get_success_url()
        return page_update

class DeleteProductos(View):
    template_name = 'productos/delete_productos.html'

    def get_success_url(self):
        """
        Devuelve la URL de redirección tras eliminar el producto.
        """
        return reverse("productos")

    def get(self, request, *args, **kwargs):
        """
        Maneja el método GET para mostrar la confirmación.
        """
        producto = get_object_or_404(Product, pk=self.kwargs['pk'])
        return render(request, 'productos/delete_productos.html', {'object': producto})


    def post(self, request, *args, **kwargs):
        """
        Maneja la solicitud POST para eliminar el producto.
        """
        producto = get_object_or_404(Product, pk=self.kwargs['pk'])
        producto.delete()

        # Prepara una respuesta con redirección usando HTMX
        page_update = HttpResponse("")
        page_update["HX-Redirect"] = self.get_success_url()
        return page_update
    
class ListStock(ListView):
    template_name='stock/main_stock.html'
    model= Stock
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AddStock(CreateView):
    template_name='stock/add_stock.html'
    model= Stock
    form_class= StockForm
    
    def get_success_url(self):
        """
        Devuelve la URL de éxito a la que se redirige después de una creación exitosa.

        Returns:
            str: La URL de redirección.
        """
        return reverse("stock")
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        # Guardamos el formulario para crear el objeto
        self.object = form.save()
        # Prepara una respuesta con redirección usando HTMX
        page_update = HttpResponse("")
        page_update["HX-Redirect"] = self.get_success_url()
        return page_update

class UpdateStock(UpdateView):
    template_name='stock/update_stock.html'
    model= Stock
    form_class= StockForm

    def get_success_url(self):
        """
        Devuelve la URL de éxito a la que se redirige después de una creación exitosa.

        Returns:
            str: La URL de redirección.
        """
        return reverse("stock") 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def form_valid(self, form):
        # Guardamos el formulario para crear el objeto
        self.object = form.save()
        # Prepara una respuesta con redirección usando HTMX
        page_update = HttpResponse("")
        page_update["HX-Redirect"] = self.get_success_url()
        return page_update

class DeleteStock(View):
    
    template_name = 'productos/delete_stock.html'

    def get_success_url(self):
        """
        Devuelve la URL de redirección tras eliminar el producto.
        """
        return reverse("stock")

    def get(self, request, *args, **kwargs):
        """
        Maneja el método GET para mostrar la confirmación.
        """
        stock = get_object_or_404(Stock, pk=self.kwargs['pk'])
        return render(request, 'stock/delete_stock.html', {'object': stock})


    def post(self, request, *args, **kwargs):
        """
        Maneja la solicitud POST para eliminar el producto.
        """
        stock = get_object_or_404(Stock, pk=self.kwargs['pk'])
        stock.delete()

        # Prepara una respuesta con redirección usando HTMX
        page_update = HttpResponse("")
        page_update["HX-Redirect"] = self.get_success_url()
        return page_update
    
    
class ListVentas(ListView):
    template_name='ventas/main_ventas.html'
    model= Venta
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Optimización: Prefetch de los productos para evitar consultas adicionales
        ventas = Venta.objects.prefetch_related(
            Prefetch(
                'productos', 
                queryset=ProductoVenta.objects.select_related('producto')
            )
        ).select_related('cliente', 'metodo_pago')
        
        context['object_list'] = ventas  # Pasamos la lista de ventas al contexto
        return context

class AddVenta(CreateView):
    template_name='ventas/add_productos.html'
    model= Venta
    form_class= VentaForm
    success_url = reverse_lazy("index")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def form_valid(self, form):
        return super().form_valid(form)
    