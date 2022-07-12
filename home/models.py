from django.db import models

class Usuario(models.Model):
    email = models.CharField(primary_key=True, max_length=50,verbose_name='Email')
    nombreUsuario = models.CharField(max_length=50,verbose_name='Nombre Usuario')
    contraUsuario = models.CharField(max_length=10,verbose_name='Contraseña')

    def __str__(self):
        return self.nombreUsuario


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id categoria')
    nombreCategoria = models.CharField(max_length=20,verbose_name='Categoria')
    

    def __str__(self):
        return self.nombreCategoria


class producto(models.Model):
    nombreProducto = models.CharField(max_length=30,verbose_name='Nombre producto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField(verbose_name='Stock')
    precio = models.IntegerField(verbose_name='Precio')
    def __str__(self):
        return self.nombreProducto


