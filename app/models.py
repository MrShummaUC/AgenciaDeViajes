from django.db import models

# Create your models here.
class Servicio(models.Model):
    codigo = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_Servicio'