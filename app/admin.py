from django.contrib import admin
from .models import *
# Register your models here.
class SeguroAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','descripcion','precio']
    search_fields = ['codigo']
    list_per_page = 10

admin.site.register(Seguro, SeguroAdmin)