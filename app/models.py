from django.db import models

# Create your models here.
class Seguro(models.Model):
    codigo = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_Seguro'

class ReporteCurso(models.Model):
    codigo = models.IntegerField(null=False,primary_key=True)
    curso = models.CharField(max_length=60)
    monto_solicitado = models.IntegerField()
    monto_depositado = models.IntegerField()
    monto_faltaltante = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'db_reporteCurso'