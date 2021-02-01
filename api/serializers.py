from rest_framework import serializers
from .models import Movie , Product


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'    