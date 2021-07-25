from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes', views.pacientes, name='Pacientes'),
    path('exames', views.exames, name='Exames'),
    path('amostras', views.amostras, name='Amostras'),
    path('relations', views.relations, name='Relações')
]