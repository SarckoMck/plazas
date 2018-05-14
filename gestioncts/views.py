from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse

class ListarInstituciones(TemplateView):
	template_name ='gestioncts/listaCTs.html'