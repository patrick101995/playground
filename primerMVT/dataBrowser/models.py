from django.db import models

# Create your models here.

class Familiar(models.Model):

    nombre=models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField()
    documento = models.IntegerField()

    def __str__(self):
        return self.nombre + " " + self.apellido