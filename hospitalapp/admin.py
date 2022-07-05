from django.contrib import admin
from .models import Paciente,Doctor, Residencia #tmb podia haber puesto * (asterisco)

#esto lo vi en la clase de mi amiga en
class PacienteAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellido", "edad")
    search_fields=("nombre", "apellido",)

class DoctorAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellido","especialidad")
    search_fields=("nombre", "apellido","especialidad")

class ResidenciaAdmin(admin.ModelAdmin):
    list_display=("especialidad", "comision", "horario")
    search_fields=("especialidad", "comision", "horario")


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Residencia, ResidenciaAdmin)


# Register your models here.
