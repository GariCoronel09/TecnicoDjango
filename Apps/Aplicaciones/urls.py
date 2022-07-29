from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('salir/',views.salir, name="salir"),
    path('registrarCliente/', views.registrarCliente),
    path('edicionCliente/<cedula>', views.edicionCliente),
    path('editarCliente/', views.editarCliente),
    path('eliminarCliente/<cedula>', views.eliminarCliente),
    path('registrarUsuario/', views.registrarUsuario),
    path('edicionUsuario/<cedula>', views.edicionUsuario),
    path('editarUsuario/', views.editarUsuario)
    
]

