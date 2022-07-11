from django.db import models


class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()

class Doctor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField( max_length=30)
    especialidad=models.CharField(max_length=30, default="")
    
    class Meta:
        verbose_name_plural= "Doctores" #visto en la clase de mi amiga otra comision
    
class Residencia (models.Model):
    especialidad = models.CharField(max_length=30)
    comision=models.IntegerField()
    horario =models.IntegerField()
    