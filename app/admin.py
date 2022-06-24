from django.contrib import admin
from .models import *
# Register your models here.
class SeguroAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','descripcion','precio']
    search_fields = ['codigo']
    list_per_page = 10

admin.site.register(Seguro, SeguroAdmin)

class RegistroViajeAdmin(admin.ModelAdmin):
    list_dislay = ['id','clienteCorreo','destinoCorreo','nAlumno','tipo','fechaViaje','datoRelevante']
    search_Fields = ['id','tipo']
    list_per_page = 4
    
admin.site.register(TipoServicio)
admin.site.register(RegistroViaje,RegistroViajeAdmin)