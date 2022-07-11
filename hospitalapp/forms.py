from django import forms


from django import forms


class pacientesformulario(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    edad=forms.IntegerField(min_value=0)

class doctoresformulario(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    especialidad=forms.CharField(max_length=20)

class residenciasformulario(forms.Form):
    especialidad=forms.CharField(max_length=20)
    comision=forms.IntegerField()
    horario=forms.IntegerField()
