from django.db import models

# Create your models here.
#Estas son las tablas de la pbase de datos (Cuidado)

class Categoria(models.Model):
    idCategoria= models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto =models.IntegerField(primary_key=True, verbose_name='id de la Producto ')
    nombreProducto =models.CharField(max_length=50, verbose_name='Nombre de la Producto ')
    imagen = models.ImageField(upload_to="media/", blank=True, null=True)
    stock = models.IntegerField(verbose_name='Stock del Producto')
    precioProducto = models.IntegerField(verbose_name='Precio de el Producto ')
    
    categoria =models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreProducto

class Cargo(models.Model):
    idCargo= models.IntegerField(primary_key=True, verbose_name='Id de Cargo')
    nombreCargo = models.CharField(max_length=50, verbose_name='Nombre de la Cargo')

    def __str__(self):
        return self.nombreCargo

class Cliente(models.Model):
    rut =models.IntegerField(primary_key=True, verbose_name='Rut del Cliente')
    dv = models.CharField(max_length=50, verbose_name='Digito Verificador')
    nombre = models.CharField(max_length=50, verbose_name='Nombre del cliente')
    appaterno = models.CharField(max_length=50, verbose_name='Apellido Paterno del cliente')
    apmaterno = models.CharField(max_length=50, verbose_name='Apellido Materno del cliente')
    email = models.CharField(max_length=50, verbose_name='Email del Cliente')
    telefono = models.IntegerField(verbose_name='Telefono')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Promociones(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descuentoProducto = models.IntegerField(verbose_name='Descuento del Producto')
    FechaExpiracion = models.DateField(verbose_name='Fecha Expiración')
    

    def __int__(self):
        return self.descuentoProducto

class Compra(models.Model):
    idCompra = models.IntegerField(primary_key=True, verbose_name='Id compra')
    nombreCliente = models.CharField(max_length=50, verbose_name='Nombre del cliente')
    precioTotal = models.IntegerField(verbose_name='Precio Total de la compra')
    fechaCompra = models.DateField(verbose_name='Fecha Compra')
    rut = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreCliente

class detalle_compra(models.Model):
    idCompra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    idProducto =  models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name='Cantidad de la compra')
    precioNeto = models.IntegerField(verbose_name='Precio neto de la compra')
    descuento = models.IntegerField(verbose_name='Porcentaje de Descuento')
    
    def __int__(self):
        return self.idProducto

class pedido(models.Model):
    idPedido = models.IntegerField(primary_key=True, verbose_name='Id Pedido')
    fechaEntrega = models.DateField(verbose_name='Fecha de Entrega')
    direccionEntrega = models.CharField(max_length=50,verbose_name='Dirección de Entrega')
    estadoEntrega = models.CharField(max_length=50,verbose_name='Estado de la Compra')
    idCompra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    idDetalleCompra = models.ForeignKey(detalle_compra, on_delete=models.CASCADE)

    def __str__(self):
        return self.estadoEntrega
    

    
