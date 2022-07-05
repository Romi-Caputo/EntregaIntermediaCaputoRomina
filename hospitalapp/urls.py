from django.urls import path
from hospitalapp import views
from .views import *

urlpatterns = [
path('', inicio, name="Inicio"),
path("Pacientes/", views.paciente, name="Pacientes"), #o view.paciente tmb puede ser 
path("Pacientes_formulario/", views.paciente_formulario, name="Pacientes_formulario"),
path("Doctores/", views.doctor, name="Doctores"),
path("Doctores_formulario/", views.doctores_formulario, name="Doctores_formulario"),
path("Residencias_formulario/", views.residencia_formulario, name="Residencias_formulario"),
path("Residencias/", views.residencia, name="Residencias"),


]