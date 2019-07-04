from django.db import models
from vote.models import VoteModel

class Propuestas(VoteModel, models.Model):
    IdPropuestas = models.AutoField(primary_key=True)
    PropuestaNombre = models.CharField(max_length=500)
    PropuestaDetalle = models.TextField(max_length=1000)

    def __str__(self):
        return "%s - %s" % (self.PropuestaNombre,self.IdPropuestas) 


