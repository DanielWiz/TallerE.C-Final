from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import UserCreationForm
from .models import Propuestas
from django.template import loader

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
    cargarPropuestas = Propuestas.objects.all()

    # votos = Propuestas.objects.values_list('IdPropuestas', flat=True)
    # total = votos.votes.count()   

    #Cargamos el archivo index.html que se encuentra en la carpeta 'templates'
    template = loader.get_template('taller/propuestas.html')

    #Creamos el nombre 'deptos' para reutilizarlo en el archivo 'index.html'
    context = {
        'propuestas': cargarPropuestas,
    }

    #Invocamos la página de respuesta 'index.html'
    return HttpResponse(template.render(context, request))

def detallePropuestas(request, propuesta_id):
	propuestaD = Propuestas.objects.get(pk=propuesta_id)
	return render(request, 'taller/propuestasDetalles.html', {'propuestaD': propuestaD})

def VotosUp(request,propuesta_id):
    user = request.user
    votos = Propuestas.objects.get(pk=propuesta_id)
    votos.votes.up(user.id)
    return render(request, 'taller/index.html', {'votos': votos})

def VotosDown(request,propuesta_id):
    user = request.user
    votos = Propuestas.objects.get(pk=propuesta_id)
    votos.votes.down(user.id)
    return render(request, 'taller/index.html', {'votos': votos})

