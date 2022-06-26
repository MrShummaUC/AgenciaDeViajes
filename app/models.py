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

class TipoServicio (models.Model):
    tipo = models.CharField(max_length=25)
    def __str__(self):
        return self.tipo
    class Meta:
        db_table = 'db_tipo_producto'    


class RegistroViaje (models.Model):
    id = models.IntegerField(null=False,primary_key=True)
    clienteCorreo = models.CharField(max_length=30)
    destinoCorreo = models.CharField(max_length=30)
    fechaViaje = models.CharField(max_length=30)
    nAlumnos = models.IntegerField()
    tipo = models.ForeignKey(TipoServicio, on_delete = models.CASCADE)
    tipoActividad = models.CharField(max_length= 30)
    datoRelevante =  models.CharField(max_length= 30)
    def __str__(self):
        return self.clienteCorreo
    class Meta:
        db_table = 'db_registro_viaje'

class ContratoCurso(models.Model):
    codigo = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    fecha = models.CharField(max_length=10)
    seguro1 = models.CharField(max_length=50)
    seguro2 = models.CharField(max_length=50)
    seguro3 = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'db_contratoCurso'
                