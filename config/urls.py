from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicules/', include('apps.vehicles.urls')),
    path('numerique/', include('apps.numerique.urls')), # Ajout de la ligne numérique
    path('', include('apps.core.urls')),
]