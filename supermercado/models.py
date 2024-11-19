from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Product(models.Model):
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Usar 2 decimales para el precio
    imagen = models.FileField(upload_to='productos/',blank=True)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

class Stock(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.producto} - {self.cantidad} - {self.fecha}'


class MetodoPago(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Venta {self.id} - {self.fecha} - {self.cliente}"

    @property
    def total(self):
        """
        Calcula el total de la venta sumando los precios de los productos de ProductoVenta.
        """
        productos_venta = self.productos.all()
        total = sum([item.precio_unitario * item.cantidad for item in productos_venta])
        return total


class ProductoVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='productos', on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto en el momento de la venta

    def __str__(self):
        return f"{self.producto.nombre} - Cantidad: {self.cantidad}"

    def save(self, *args, **kwargs):
        """
        Al guardar la venta, asegurarse de registrar el precio actual del producto en precio_unitario
        """
        if not self.precio_unitario:
            self.precio_unitario = self.producto.precio
        super().save(*args, **kwargs)
