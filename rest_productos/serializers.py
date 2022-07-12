from rest_framework import serializers
from home.models import producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = ['nombreProducto','categoria','stock','precio']