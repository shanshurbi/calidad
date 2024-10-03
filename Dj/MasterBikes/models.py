from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True, db_column="idTipoUsuario")
    tipo = models.CharField(max_length=30, db_column="Tipo de Usuario")
    descripcion = models.CharField(max_length=60)

    def __str__(self):
        return (
            str(self.tipo)
        )

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(primary_key=True, max_length=10)
    id_tipo_usuario = models.ForeignKey(
        "TipoUsuario", on_delete=models.CASCADE, db_column="idTipoUsuario"
    )

    def __str__(self):
        return (
            str(self.rut)
        )

class Talla(models.Model):
    id_talla = models.AutoField(primary_key=True, db_column="idTalla")
    talla = models.CharField(max_length=10)
    def __str__(self):
        return (
            str(self.talla)
        )

class TipoBici(models.Model):
    id_tipo_bici = models.AutoField(primary_key=True, db_column="idTipoBici")
    tipo = models.CharField(max_length=30)
    def __str__(self):
        return (
            str(self.tipo)
        )

class FormaPago(models.Model):
    id_forma_pago = models.AutoField(primary_key=True, db_column="idFormaPago")
    forma = models.CharField(max_length=30)
    def __str__(self):
        return (
            str(self.forma)
        )
    class Meta:
        verbose_name_plural = "Formas de pago"

class Arriendo(models.Model):
    id_arriendo = models.AutoField(primary_key=True, db_column="idArriendo")
    rut = models.ForeignKey(
        "Usuario", on_delete=models.CASCADE, db_column="rut"
    )
    direccion = models.CharField(max_length=80)
    id_tipo_bici = models.ForeignKey(
        "TipoBici", on_delete=models.CASCADE, db_column="idTipoBici"
    )
    id_talla = models.ForeignKey(
        "Talla", on_delete=models.CASCADE, db_column="idTalla"
    )
    inicio = models.DateField()
    termino = models.DateField()
    id_forma_pago = models.ForeignKey(
        "FormaPago", on_delete=models.CASCADE, db_column="idFormaPago"
    )


    def __str__(self):
        return (
            str(self.id_arriendo)
            + " "
            + str(self.rut)
        )

class TipoProducto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True, db_column="idTipoProducto")
    tipo = models.CharField(max_length=30)
    def __str__(self):
        return (
            str(self.tipo)
        )

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, db_column="idProducto")
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30, null=True, blank=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    id_tipo_producto = models.ForeignKey(
        "TipoProducto", on_delete=models.CASCADE, db_column="idTipoProducto"
    )
    foto = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return (
            str(self.id_producto)
            + " "
            + str(self.nombre)
        )

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True, db_column="idEstado")
    tipo = models.CharField(max_length=30)
    def __str__(self):
        return (
            str(self.tipo)
        )

class Reparacion(models.Model):
    id_reparacion = models.AutoField(primary_key=True, db_column="idReparacion")
    rut = models.ForeignKey(
        "Usuario", on_delete=models.CASCADE, db_column="rut"
    )
    modelo_bicicleta = models.CharField(max_length=80)
    problema = models.CharField(max_length=150, blank=True, null=True)
    id_estado = models.ForeignKey(
        "Estado", on_delete=models.CASCADE, db_column="idEstado"
    )
    fecha = models.DateTimeField()
    def __str__(self):
        return(
            str(self.id_reparacion)
            + " "
            + str(self.modelo_bicicleta)
            + " "
            + str(self.rut)
        )
    class Meta:
        verbose_name_plural = "Reparaciones"
    
class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True, db_column="idPago")
    rut = models.ForeignKey(
        "Usuario", on_delete=models.CASCADE, db_column="rut"
    )
    total = models.IntegerField()
    id_forma_pago = models.ForeignKey(
        "FormaPago", on_delete=models.CASCADE, db_column="idFormaPago"
    )
    domicilio = models.BooleanField()

class Detalle(models.Model):
    id_detalle = models.AutoField(primary_key=True, db_column="idDetalle")
    id_pago = models.ForeignKey(
        "Pago", on_delete=models.CASCADE, db_column="idPago"
    )
    id_producto = models.ForeignKey(
        "Producto", on_delete=models.CASCADE, db_column="idProducto"
    )
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    
class Despacho(models.Model):
    id_despacho = models.AutoField(primary_key=True, db_column="idDespacho")
    id_pago = models.ForeignKey(
        "Pago", on_delete=models.CASCADE, db_column="idPago"
    )
    pedido = models.DateTimeField(blank=True,null=True)
    envio = models.DateTimeField(blank=True,null=True)
    recibo = models.DateTimeField(blank=True,null=True)

class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True, db_column="idCarrito")
    rut = models.ForeignKey(
        "Usuario", on_delete=models.CASCADE, db_column="rut"
    )

class Item(models.Model):
    id_item = models.AutoField(primary_key=True, db_column="idItem")
    id_carrito = models.ForeignKey(
        "Carrito", on_delete=models.CASCADE, db_column="idCarrito"
    )
    id_producto = models.ForeignKey(
        "Producto", on_delete=models.CASCADE, db_column="idProducto"
    )
    cantidad = models.IntegerField()
    subtotal = models.IntegerField(null=True,blank=True)