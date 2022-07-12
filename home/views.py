from django import forms
from django.shortcuts import render, redirect
from .models import Usuario, Categoria, producto
from .forms import ProductoForm, UsuarioForm

# Create your views here.

def index(request):
    return render(request,'home/index.html')

def contacto(request):
    return render(request,'home/contacto.html')

def inicio_sesion(request):
    datos = {
        'form' :  UsuarioForm()
    }
    if (request.method == 'POST'):
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save() #insert a la BD
            datos['mensaje'] = 'usuario se guardó'
        else:
            datos['mensaje'] = 'usuario NO se guardó'
  
    return render(request,'home/inicio_sesion.html', datos)


def carrito(request):
    listaProducto = producto.objects.all()
    datos = {
        'productos': listaProducto
    }
    return render(request,'home/carrito.html', datos)

def modificar_usuario(request, id):
    usuario = Usuario.objects.get(email=id) 
    datos = {
        'form': UsuarioForm(instance=usuario)
    }
    if (request.method == 'POST'):
        formulario = UsuarioForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save() 
            datos['mensaje'] = 'Usuario se modificó'
        else:
            datos['mensaje'] = 'Usuario NO se modificó'

    return render(request,'home/modificar_usuario.html', datos)



def listaUsuarios(request):
    listaUsuario = Usuario.objects.all()
    datos = {
        'usuarios': listaUsuario
    }
    return render(request,'home/inicio_sesion.html', datos)


def modificar_stock(request, id):
    productos = producto.objects.get(nombreProducto=id) 
    datos = {
        'form': ProductoForm(instance=productos)
    }
    if (request.method == 'POST'):
        formulario = ProductoForm(data=request.POST, instance=productos)
        if formulario.is_valid():
            formulario.save() 
            datos['mensaje'] = 'Stock se modificó'
        else:
            datos['mensaje'] = 'Stock NO se modificó'

    return render(request,'home/modificar_stock.html', datos)

def eliminar_producto(request, id):
    productos = producto.objects.get(nombreProducto=id)
    productos.delete() # delete from Vehiculo where patente = id

    return redirect(to='carrito')