from django.db import models

# Create your models here.
class Cliente(models.Model):
    cedula = models.CharField(max_length=11)
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    
    def __str__(self):
        return self.cedula

class Usuario(models.Model):
    cedula = models.CharField(max_length=11)
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    rol =  models.CharField(max_length= 50)
        
    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    codigo = models.CharField(max_length=11)
    descripcion= models.CharField(max_length=50)
    precio= models.IntegerField(default=0)
    tipo= models.CharField(max_length=50)
    def __str__(self):
        return self.codigo

class Equipo(models.Model):
    codigo = models.CharField(max_length=11)
    nro_serie= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    color= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo

class Orden(models.Model):
    codigoOrden = models.CharField(max_length=11)
    fechaIngreso = models.CharField(max_length=50)
    fechaSalida= models.CharField(max_length=50)
    observaciones= models.CharField(max_length=250)
    accesorios= models.CharField(max_length=250)
    encargado = models.CharField(max_length=250)
    totalPago = models.IntegerField(default=0)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigoOrden

