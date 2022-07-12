from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from home.models import producto
from rest_productos.serializers import ProductoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listaProducto(request):
    if request.method == 'GET':
        listaProducto = producto.objects.all()
        serializ = ProductoSerializer(listaProducto, many = True)
        return Response(serializ.data)
    elif request.method == 'POST':
        dataV = JSONParser().parse(request)
        serializ = ProductoSerializer(data = dataV)
        if serializ.is_valid():
            serializ.save()
            return Response(serializ.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializ.errors, status = status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_producto(request, pat):
    try:
        productos = producto.objects.get(nombreProducto=pat) 
    except productos.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializ = ProductoSerializer(producto)
        return Response(serializ.data)
    elif request.method == "PUT":
        dataV = JSONParser().parse(request)
        serializ = ProductoSerializer(productos, data = dataV)
        if serializ.is_valid():
            serializ.save()
            return Response(serializ.data)
        else:
            return Response(serializ.errors, status = status.HTTP_400_BAD_REQUEST) 
    elif request.method == "DELETE":
        productos.delete() # DELETE A LA BD
        return Response(status = status.HTTP_204_NO_CONTENT) 
