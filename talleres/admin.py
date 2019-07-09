from django.contrib import admin
from .models import Propuesta,Taller,PropuestaAprobada

admin.site.register(Taller)
admin.site.register(Propuesta)
admin.site.register(PropuestaAprobada)