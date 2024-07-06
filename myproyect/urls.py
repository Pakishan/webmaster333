# En tu archivo urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    # Otras URLS de tu aplicación
]
