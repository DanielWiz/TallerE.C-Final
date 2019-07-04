from django.db import models
from vote.models import VoteModel
from datetime import datetime

class Propuestas(VoteModel, models.Model):
    IdPropuestas = models.AutoField(primary_key=True)
    PropuestaNombre = models.CharField(max_length=500)
    PropuestaDetalle = models.TextField(max_length=1000)

    def __str__(self):
        return "%s - %s" % (self.PropuestaNombre,self.IdPropuestas) 

class Taller(models.Model):
	codigo_taller = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=60)
	descripcion = models.CharField(max_length=120)
	fecha = models.DateTimeField(default=datetime.now())
	lugar_taller = models.CharField(max_length=60)
	def __str__(self):
		return "%s. %s" % (self.codigo_taller, self.nombre)


