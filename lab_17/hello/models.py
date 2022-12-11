from django.db import models
class Brend(models.Model):
    name_brend=models.CharField(max_length=50)
    country=models.CharField(max_length=50)

class Stock(models.Model):
    name_stock=models.CharField(max_length=50)
    start_stock=models.CharField(max_length=50)
    finish_stock = models.CharField(max_length=50)
    persent_stock = models.CharField(max_length=50)

class Product(models.Model):
    name_product=models.CharField(max_length=50)
    catagory=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    brend=models.ForeignKey(Brend, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

# Create your models here.
