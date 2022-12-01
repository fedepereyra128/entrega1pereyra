from django.db import models

# Create your models here.


class Auto(models.Model):
    marca=models.CharField(max_length=30)
    patente=models.IntegerField()
    modelo=models.CharField(max_length=30)

    def __str__(self):
        return self.marca+""+str(self.patente)+""+self.modelo


class Motos(models.Model):
    marca=models.CharField(max_length=30)
    cilindrada=models.IntegerField()
    tipo=models.CharField(max_length=30)

    def __str__(self):
        return self.marca+""+str(self.cilindrada)+""+self.tipo

class Pickup_suv(models.Model):
    marca=models.CharField(max_length=30)
    tipo_motor=models.CharField(max_length=30)
    rodado=models.IntegerField()

    def __str__(self):
        return self.marca+""+str(self.rodado)+""+(self.tipo_motor)
