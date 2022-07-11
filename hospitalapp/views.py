from doctest import ELLIPSIS_MARKER
from urllib import request
from django.shortcuts import redirect, render

from .models import Doctor, Paciente, Residencia
from .forms import pacientesformulario, doctoresformulario, residenciasformulario


def inicio(request):
      return render(request, "hospitalapp/Inicio.html",{"inicio":inicio})

def paciente(request):
      paciente = Paciente.objects.all()
      return render(request, "hospitalapp/Pacientes.html", {"paciente":paciente})

def doctor(request):
      doctor = Doctor.objects.all()
      return render(request, "hospitalapp/Doctores.html",{"doctor": doctor})

def residencia(request):
      residencia = Residencia.objects.all()
      return render(request, "hospitalapp/Residencias.html", {"residencia": residencia})


def crear_paciente(request):
    
    # post
    if request.method == "POST":
        
        formulario = pacientesformulario(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            paciente = Paciente(nombre=info["nombre"],apellido=info["apellido"],edad=info["edad"])
            paciente.save()

            return redirect("Pacientes")

        return render(request,"hospitalapp/pacientes_formulario.html",{"form":formulario})

    # get
    formulario = pacientesformulario()
    return render(request,"hospitalapp/pacientes_formulario.html",{"form":formulario})

def crear_doctor(request):
    
    # post
    if request.method == "POST":
        
        formulario = doctoresformulario(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            doctores = Doctor(nombre=info["nombre"],apellido=info["apellido"],especialidad=info["especialidad"])
            doctores.save()

            return redirect("Doctores")

        return render(request,"hospitalapp/doctores_formulario.html",{"form":formulario})

    # get
    formulario = doctoresformulario()
    return render(request,"hospitalapp/doctores_formulario.html",{"form":formulario})

def crear_residencia(request):
    
    # post
    if request.method == "POST":
        
        formulario = residenciasformulario(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            residencia = Residencia(especialidad=info["especialidad"],comision=info["comision"],horario=info["horario"])
            residencia.save()

            return redirect("Residencias")

        return render(request,"hospitalapp/residencias_formulario.html",{"form":formulario})

    # get
    formulario = residenciasformulario()
    return render(request,"hospitalapp/residencias_formulario.html",{"form":formulario})

    
def buscar_pacientes(request):
    if request.method == "POST":

        info_paciente = request.POST["apellido"]
        
        paciente = Paciente.objects.filter(apellido__icontains=info_paciente)
        

        return render(request,"hospitalapp/buscar_pacientes.html",{"paciente":paciente})

    else: # get y otros

        paciente =  []  
        
        return render(request,"hospitalapp/buscar_pacientes.html",{"paciente":paciente})


    