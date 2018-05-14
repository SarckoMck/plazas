"""asignacion_plazas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from books.views import OneBook, get_name, registro_autor, registro_libro

    path('your-name/', get_name, name="Your Name"),
    path('nuevo-autor/', registro_autor, name="Nuevo Autor"),
    path('nuevo-libro/', registro_libro, name="Nuevo Libro"),

"""
from django.contrib import admin
from django.urls import path

from gestiondocentes.views import ListarDocentes
from gestioncts.views import ListarInstituciones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listadocentes/', ListarDocentes.as_view(),name= "listarDocentes"),
    path('listadocts/', ListarInstituciones.as_view(),name= "listarCTs"),
  ]

admin.site.site_header = 'Sistema de Asignación de Plazas [SAP]'
admin.site.site_title = 'Dirección de Educación'
admin.site.index_titlle = 'Dirección de Educación'