from django.shortcuts import render, redirect
from .models import Equipo, Usuario
from .models import Cliente
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
#def home(request):
#    return render(request, 'inicio.html')
@login_required

def salir(request):
    logout(request)
    return redirect('/')
    
def home(request):
    usuarioLista = Cliente.objects.all()
    return render(request, "cliente.html", {"cliente":usuarioLista})

def cliente_template(request):
    clienteLista = Cliente.objects.all()
    return render(request, "cliente.html", {"cliente":clienteLista})

def usuario_template(request):
    usuarioLista = Usuario.objects.all()
    return render(request, "usuario.html", {"usuario":usuarioLista})

def equipo_template(request):
    equipoLista = Equipo.objects.all()
    return render(request, "equipo.html", {"equipo":equipoLista})

# CRUD DE CLIENTES
def registrarCliente(request):
    cedula = request.POST['txtCedula']
    nombre =  request.POST['txtNombre']
    apellido =  request.POST['txtApellido']
    direccion =  request.POST['txtDireccion']
    telefono =  request.POST['txtTelefono']

    cliente = Cliente.objects.create(cedula = cedula, nombre= nombre, 
    apellido = apellido, direccion = direccion,  telefono= telefono)
    return redirect('/')

#editar Cliente
def edicionCliente(request, cedula):
    cliente = Cliente.objects.get(cedula=cedula)
    return render(request, "editarCliente.html", {"cliente": cliente})

def editarCliente(request):
    cedula = request.POST['txtCedula']
    nombre =  request.POST['txtNombre']
    apellido =  request.POST['txtApellido']
    direccion =  request.POST['txtDireccion']
    telefono =  request.POST['txtTelefono']
    
    cliente = Cliente.objects.get(cedula = cedula)
    cliente.nombre= nombre 
    cliente.apellido = apellido
    cliente.direccion = direccion
    cliente.telefono= telefono
    cliente.save()

    return redirect('/')

#eliminar Cliente
def eliminarCliente(request, cedula):
    cliente = Cliente.objects.get(cedula=cedula)
    cliente.delete()
    return redirect('/')

#CRUD DE USUARIOS
def registrarUsuario(request):
    cedula = request.POST['txtCedula']
    nombre =  request.POST['txtNombre']
    apellido =  request.POST['txtApellido']
    direccion =  request.POST['txtDireccion']
    telefono =  request.POST['txtTelefono']
    rol = request.POST['txtrol']

    usuario = Usuario.objects.create(cedula = cedula, nombre= nombre, 
    apellido = apellido, direccion = direccion,  telefono= telefono, rol = rol)
    return redirect('/')

def edicionUsuario(request, cedula):
    usuario = Usuario.objects.get(cedula=cedula)
    return render(request, "editarUsuario.html", {"usuario": usuario})

def editarUsuario(request):
    cedula = request.POST['txtCedula']
    nombre =  request.POST['txtNombre']
    apellido =  request.POST['txtApellido']
    direccion =  request.POST['txtDireccion']
    telefono =  request.POST['txtTelefono']
    rol = request.POST['txtrol']
    
    usuario = Usuario.objects.get(cedula = cedula)
    usuario.nombre= nombre 
    usuario.apellido = apellido
    usuario.direccion = direccion
    usuario.telefono= telefono
    usuario.rol = rol
    usuario.save()

    return redirect('/')