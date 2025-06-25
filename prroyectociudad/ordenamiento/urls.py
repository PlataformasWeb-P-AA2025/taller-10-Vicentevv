from django.urls import path
from . import views

urlpatterns = [
    path('parroquias/', views.lista_parroquias, name='lista_parroquias'),
    path('barrios/', views.lista_barrios, name='lista_barrios'),
    path('crear_parroquia/', views.crear_parroquia, name='crear_parroquia'),
    path('crear_barrio/', views.crear_barrio, name='crear_barrio'),
]
