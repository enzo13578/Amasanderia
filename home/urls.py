from django.urls import path, include
from .views import  index,contacto,carrito,inicio_sesion,modificar_usuario,modificar_stock,listaUsuarios,eliminar_producto

urlpatterns = [
    path('', index,name="index"),
    path('contacto/', contacto,name="contacto"),
    path('carrito', carrito,name="carrito"),
    path('inicio_sesion', inicio_sesion,name="inicio_sesion"),
    path('modificar_usuario/<id>',modificar_usuario,name="modificar_usuario"),
    path('modificar_stock/<id>',modificar_stock,name="modificar_stock"),
    path('listaUsuarios',listaUsuarios,name="listaUsuarios"),
    path('eliminar_producto/<id>',eliminar_producto,name="eliminar_producto"),
]