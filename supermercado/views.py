from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, FormView, ListView,
                                  TemplateView, UpdateView)

from.models import Product,Stock,Venta
from .froms import ConfirmDeleteForm, ProductoForm, StockForm, VentaForm

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
    success_url = reverse_lazy("stock")
    
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
    
class ListVentas(ListView):
    template_name='ventas/main_ventas.html'
    model= Venta
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
    