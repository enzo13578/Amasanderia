from django.urls import path, include
from rest_productos.views import listaProducto, detalle_producto
from rest_productos.viewsLogin import login, logout

urlpatterns = [
    path('listaProducto',listaProducto,name="listaProducto"),
    path('detalle_producto/<pat>',detalle_producto,name="detalle_producto"),
    path('login',login,name="login_html"),
    path('logout',logout,name="logout_html"),
]
