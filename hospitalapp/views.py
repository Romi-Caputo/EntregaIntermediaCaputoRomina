from urllib import request
from django.shortcuts import redirect, render
from .models import Doctor, Paciente, Residencia
from .forms import Nuevaresidencia, Nuevodoctor, Nuevopaciente




# Create your views here.
def inicio(request):
      return render(request, "hospitalapp/Inicio.html")

def paciente(request):
      paciente = Paciente.objects.all()
      return render(request, "hospitalapp/Pacientes.html", {"paciente":paciente})

def paciente_formulario(request):
      if request.method == "POST":
            paciente= Paciente(request.POST ["nombre"],request.POST ["apellido"],request.POST["edad"] )
            paciente.save
            return redirect("Pacientes")
      else:
            formulariovacio=Nuevopaciente()
            return render(request, "hospitalapp/formulario_pacientes.html", {"form": formulariovacio})     


def doctor(request):
      doctor = Doctor.objects.all()
      return render(request, "hospitalapp/Doctores.html",{"doctor": doctor})

def doctores_formulario(request):
      if request.method == "POST":
            doctor= Doctor(request.POST ["nombre"],request.POST ["apellido"],request.POST["especialidad"] )
            doctor.save
            return redirect("Doctores")
      else:
            formulariovacio=Nuevodoctor()
            return render (request, "hospitalapp/formulario_doctores.html",{"form": formulariovacio})

def residencia(request):
      residencia = Residencia.objects.all()
      return render(request, "hospitalapp/Residencias.html", {"residencia": residencia})

def residencia_formulario(request):
      if request.method == "POST":
            residencia= Residencia(request.POST ["especialidad"],request.POST ["comision"],request.POST["horario"] )
            residencia.save
            return redirect ("Residencias")
      else:
            formulariovacio=Nuevaresidencia()
            return render (request, "hospitalapp/formulario_residencias.html",{"form": formulariovacio})



