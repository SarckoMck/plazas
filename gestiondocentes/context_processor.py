from django.urls import reverse
from gestiondocentes.models import *

def docentes_data(request):
		if 'admin' in request.META['PATH_INFO']:
			return {}
		else:
			listaDocs = Docente.objects.all()
			return {'list_docs': listaDocs } 