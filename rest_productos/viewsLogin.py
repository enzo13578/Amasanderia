from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    v_username = data['username']
    v_password = data['password']
    try:
        usuario = User.objects.get(username = v_username)
    except User.DoesNotExist:
        return Response("Usuario Inválido")
    
    pass_valido = check_password(v_password, usuario.password)
    
    if not pass_valido:
        return Response("Password Incorrecta")
    
    token, created = Token.objects.get_or_create(user=usuario)
    return Response(token.key)

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render_to_response('index.html', {}, RequestContext(request))

