from django.shortcuts import render
from .models import Parroquia, Barrio
from .forms import ParroquiaForm, BarrioForm


def lista_parroquias(request):
    parroquias = Parroquia.objects.all()
    return render(request, 'ordenamiento/lista_parroquias.html', {'parroquias': parroquias})

def lista_barrios(request):
    barrios = Barrio.objects.all()
    return render(request, 'ordenamiento/lista_barrios.html', {'barrios': barrios})


def crear_parroquia(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_parroquias')
    else:
        form = ParroquiaForm()
    return render(request, 'ordenamiento/crear_parroquia.html', {'form': form})

def crear_barrio(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_barrios')
    else:
        form = BarrioForm()
    return render(request, 'ordenamiento/crear_barrio.html', {'form': form})
