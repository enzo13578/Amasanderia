from django import forms
from django.forms import ModelForm
from .models import Usuario, producto

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['email','nombreUsuario','contraUsuario']


class ProductoForm(ModelForm):
    class Meta:
        model = producto
        fields = ['stock']


