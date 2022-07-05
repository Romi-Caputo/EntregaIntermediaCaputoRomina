from unittest.util import _MAX_LENGTH
from django import forms

class Nuevopaciente(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30, )
    edad= forms.IntegerField()

class Nuevodoctor(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    especialidad= forms.CharField(max_length=30)

class Nuevaresidencia(forms.Form):
    especialidad= forms.CharField(max_length=30)
    comision= forms.IntegerField( )
    horario= forms.IntegerField()