from pyexpat import model
from django.contrib import admin
from .models import *

# Register your models here.
class AdminUsuario(admin.ModelAdmin):
    list_display = ["__str__","cedula","nombre","apellido","direccion","telefono","rol"]
    class Meta(object):
        model = Usuario
admin.site.register(Usuario,AdminUsuario)

class AdminCliente(admin.ModelAdmin):
     list_display = ["__str__","cedula","nombre","apellido","direccion","telefono"]
     class Meta(object):
        model = Cliente
admin.site.register(Cliente,AdminCliente)

class AdminServicio(admin.ModelAdmin):
     list_display = ["__str__","codigo","descripcion","precio","tipo"]
     class Meta(object):
        model = Servicio
admin.site.register(Servicio,AdminServicio)

class adminEquipo(admin.ModelAdmin):
     list_display = ["__str__","codigo","nro_serie","modelo","color","descripcion","cliente"]
     class Meta(object):
        model = Equipo
admin.site.register(Equipo,adminEquipo)

class AdminOrden(admin.ModelAdmin):
     list_display = ["__str__","codigoOrden","fechaIngreso","fechaSalida","observaciones","accesorios","encargado","totalPago","equipo","servicio"]
     class Meta(object):
        model = Orden
admin.site.register(Orden,AdminOrden)

