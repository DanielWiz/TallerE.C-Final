from django.urls import path, include
from talleres import views as core_views
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('', include('social_django.urls', namespace='social')),
    path('login/', views.cargarLogin, name='cargarLogin'),
    path('registro/', core_views.signup, name='signup'),
    path('talleres',views.talleres, name='talleres'),
    path('propuestas',views.cargarPropuestas, name='cargarPropuestas'),
    path('mapa',views.mapa,name='mapa'),
    path('politica',views.cargarPolitica,name='cargarPolitica'),
    path('propuesta/<int:propuesta_id>', views.detallePropuestas, name='propuestaD'),
    path('propuvoto/<int:propuesta_id>', views.VotosUp, name='votosUp'),
    path('propunovoto/<int:propuesta_id>', views.VotosDown, name='votosDown'),
]