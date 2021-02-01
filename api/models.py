from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    title=models.CharField(max_length=50)
    genre=models.TextField(max_length=50)
    description=models.TextField(max_length=100)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])


class Product(models.Model):
    productType=models.CharField(max_length=50)
    productName=models.CharField(max_length=50)
    mrpPrice=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10000000)]) 
    salesPrice=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10000000)])    



