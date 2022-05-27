from django.contrib import admin
from ajana_mehdi.views import *

# Register your models here.
@admin.register(Patient)
@admin.register(Medecin)
@admin.register(RendezVous)
@admin.register(Consultation)

class PatientAdmin(admin.ModelAdmin):
    pass

class MedecinAdmin(admin.ModelAdmin):
    pass

class RendezVousAdmin(admin.ModelAdmin):
    pass

class ConsultationAdmin(admin.ModelAdmin):
    pass