from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import UserCreationForm
from .models import Propuesta, Taller, PropuestaAprobada
from django.template import loader
from django.contrib.auth.decorators import user_passes_test

def index(request):
    return render(request, 'taller/index.html', {})

def talleres(request):
    return render(request, 'taller/talleres.html', {})

def cargarPropuestas(request):
    return render(request, 'taller/propuestas.html', {})

def mapa(request):
    return render(request, 'taller/mapa.html', {})

def cargarLogin(request):
    return render(request, 'registration/login.html')

def cargarRegistro(request):
	return render(request, 'registration/registro.html')

def cargarPolitica(request):
    return render(request, 'taller/export.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

def cargarPropuestas(request):  
    #Obtenemos los departamentos ordenados de manera descendente.
    #[Z-A] Se antepone el signo menos (-)
    cargarPropuestasAprobadas = PropuestaAprobada.objects.all()

    # votos = Propuestas.objects.values_list('IdPropuestas', flat=True)
    # total = votos.votes.count()   

    #Cargamos el archivo index.html que se encuentra en la carpeta 'templates'
    template = loader.get_template('taller/propuestas.html')

    #Creamos el nombre 'deptos' para reutilizarlo en el archivo 'index.html'
    context = {
        'propuestasaprobadas': cargarPropuestasAprobadas,
    }

    #Invocamos la página de respuesta 'index.html'
    return HttpResponse(template.render(context, request))

def talleres(request):  
    #Obtenemos los departamentos ordenados de manera descendente.
    #[Z-A] Se antepone el signo menos (-)
    cargarTalleres = Taller.objects.all()

    #Cargamos el archivo index.html que se encuentra en la carpeta 'templates'
    template = loader.get_template('taller/talleres.html')

    #Creamos el nombre 'deptos' para reutilizarlo en el archivo 'index.html'
    context = {
        'talleres': cargarTalleres,
    }

    #Invocamos la página de respuesta 'index.html'
    return HttpResponse(template.render(context, request))  

def detallePropuestas(request, propuesta_id):
	propuestaD = PropuestaAprobada.objects.get(pk=propuesta_id)
	return render(request, 'taller/propuestasDetalles.html', {'propuestaD': propuestaD})

def VotosUp(request,propuesta_id):
    user = request.user
    votos = PropuestaAprobada.objects.get(pk=propuesta_id)
    votos.votes.up(user.id)
    return redirect("/propuestas")

def VotosDown(request,propuesta_id):
    user = request.user
    votos = PropuestaAprobada.objects.get(pk=propuesta_id)
    votos.votes.down(user.id)
    return redirect("/propuestas")

def agregarNuevaPropuesta(request):
    return render(request, 'taller/formularioPropuesta.html')

def guardarNuevaPropuesta(request):
    PropuestaNombre = request.POST['txtNombrePropuesta']
    PropuestaDetalle = request.POST['txtDetallePropuesta']
    p = Propuesta(PropuestaNombre = PropuestaNombre, PropuestaDetalle = PropuestaDetalle)
    p.save()
    return render(request, 'taller/guardarNuevaPropuesta.html', {'PropuestaNombre':PropuestaNombre})

@user_passes_test(lambda u: u.is_superuser)
def propuestasParaAprobar(request):
    #Obtenemos los departamentos ordenados de manera descendente.
    #[Z-A] Se antepone el signo menos (-)
    cargarPropuestas = Propuesta.objects.all()

    # votos = Propuestas.objects.values_list('IdPropuestas', flat=True)
    # total = votos.votes.count()   

    #Cargamos el archivo index.html que se encuentra en la carpeta 'templates'
    template = loader.get_template('taller/listadoPropuestasParaAprobar.html')

    #Creamos el nombre 'deptos' para reutilizarlo en el archivo 'index.html'
    context = {
        'propuestas': cargarPropuestas,
    }

    #Invocamos la página de respuesta 'index.html'
    return HttpResponse(template.render(context, request))

def confirmarPropuestaParaAprobar(request, propuesta_id):
    propuestaD = Propuesta.objects.get(pk=propuesta_id)
    return render(request, 'taller/confirmarPropuestaParaAprobar.html', {'propuestaD': propuestaD})

def confirmarEliminarPropuestaParaAprobar(request, propuesta_id):
    propuestaD = Propuesta.objects.get(pk=propuesta_id)
    return render(request, 'taller/confirmarEliminarPropuestaParaAprobar.html', {'propuestaD': propuestaD})

def guardarPropuestaAprobada(request, propuesta_id):
    propuestaBorrar = Propuesta.objects.get(pk=propuesta_id)
    PropuestaAprobadaNombre=request.POST['txtNombrePropuestaAprobada']
    PropuestaAprobadaDetalle= request.POST['txtDetallePropuestaAprobada']
    pa = PropuestaAprobada(PropuestaAprobadaNombre = PropuestaAprobadaNombre, PropuestaAprobadaDetalle = PropuestaAprobadaDetalle)
    pa.save()
    propuestaBorrar.delete()
    return render(request, 'taller/guardarPropuestaAprobada.html', {'PropuestaAprobadaNombre': PropuestaAprobadaNombre})

def eliminarPropuestaParaAprobar(request, propuesta_id):
    propuestaBorrar = Propuesta.objects.get(pk=propuesta_id)
    propuestaBorrar.delete()
    return render(request, 'taller/eliminarPropuestaParaAprobar.html')