from django.db import models

class Parroquia(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=50, choices=[('Norte', 'Norte'), ('Sur', 'Sur'), ('Este', 'Este'), ('Oeste', 'Oeste')])
    tipo = models.CharField(max_length=10, choices=[('urbana', 'Urbana'), ('rural', 'Rural')])

    def __str__(self):
        return self.nombre

class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    numero_viviendas = models.IntegerField()
    numero_parques = models.IntegerField(choices=[(i, i) for i in range(1, 7)])
    numero_edificios_residenciales = models.IntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name='barrios')

    def __str__(self):
        return self.nombre
