from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView

from.models import Product,Stock,Venta
from .froms import ProductoForm

# Create your views here.

class IndexView(TemplateView):
    template_name= 'index.html'
    
class ListProductos(ListView):
    template_name='productos/main_productos.html'
    model= Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class AddProductos(CreateView):
    template_name='productos/add_productos.html'
    model= Product
    # form_class= 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def form_valid(self, form):
        return super().form_valid(form)
    
    
    

class ListStock(ListView):
    template_name='stock/main_stock.html'
    model= Stock
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class ListVentas(ListView):
    template_name='ventas/main_ventas.html'
    model= Venta
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context