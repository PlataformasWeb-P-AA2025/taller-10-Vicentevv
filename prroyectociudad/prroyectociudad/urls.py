from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ordenamiento/', include('ordenamiento.urls')),  # Aquí se incluye las URLs de la app 'ordenamiento'
]
