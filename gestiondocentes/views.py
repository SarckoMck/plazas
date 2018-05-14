from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse

class ListarDocentes(TemplateView):
	template_name ='gestiondocentes/listaDocentes.html'
