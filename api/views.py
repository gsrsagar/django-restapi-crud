from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import MovieSerializer,ProductSerializer
from .models import Movie, Product


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    


#For both Product, Movie objects we can perform crud operations

#URL: localhost:8000/api/movie
#URL: localhost:8000/api/product