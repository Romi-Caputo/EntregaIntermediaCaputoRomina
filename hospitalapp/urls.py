from django.urls import path
from hospitalapp import views


urlpatterns = [
path('', views.inicio, name="Inicio"),
path("Pacientes/", views.paciente, name="Pacientes"),
path("Doctores/", views.doctor, name="Doctores"),
path("Residencias/", views.residencia, name="Residencias"),
path("Pacientesformulario/", views.crear_paciente, name="Pacientesformularios"),
path("Doctoresformulario/", views.crear_doctor, name="Doctoresformularios"),
path("Residenciaformulario/", views.crear_residencia, name="Residenciaformularios"),
path("Buscarpacientes/", views.buscar_pacientes, name="Buscarpacientes"),



]