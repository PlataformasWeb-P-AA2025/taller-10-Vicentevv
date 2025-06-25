from django.contrib import admin
from .models import Parroquia, Barrio

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre',)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia')
    search_fields = ('nombre',)

# Asegúrate de que no estés registrando más de una vez el mismo modelo
admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Barrio, BarrioAdmin)
