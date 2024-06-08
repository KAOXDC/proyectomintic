from django.urls import path
from .views import *

urlpatterns = [
    path('', pagina_inicio_view),
    path('biografia', biografia_view),
    path('proyectos', proyectos_view),
]