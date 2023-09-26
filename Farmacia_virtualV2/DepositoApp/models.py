from django.db import models

# Create your models here.
class Medicacion(models.Model):
    nombre =models.CharField(max_length=40)
    laboratorio =models.IntegerField()

class Laboratorio(models.Model):
    nombre= models.CharField(max_length=30)
    direccion= models.CharField(max_length=50)
    email = models.EmailField()

class Pedidos(models.Model):
    laboratorio = models.CharField(max_length=40)
    fechaEntrega= models.DateField()