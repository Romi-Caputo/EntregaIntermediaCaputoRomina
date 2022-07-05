from django.db import models


class Paciente(models.Model):
    nombre = models.CharField("Nombre del Paciente", max_length=30)
    apellido = models.CharField("Apellido del Paciente", max_length=30)
    edad = models.PositiveIntegerField("Edad del Paciente") #edades mayores de 0

class Doctor(models.Model):
    nombre= models.CharField("Nombre del Doctor", max_length=30)
    apellido= models.CharField("Apellido del Doctor", max_length=30)
    especialidad=models.CharField("Especialidad del Doctor",max_length=30, default="")
    

    class Meta:
        verbose_name_plural= "Doctores" #visto en la clase de mi amiga otra comision
    
class Residencia (models.Model):
    especialidad = models.CharField("Nombre de la Especialidad", max_length=30)
    comision=models.IntegerField("Comisión")
    horario =models.IntegerField("Horario")
    