from django.urls import reverse
from gestioncts.models import *

def ct_data(request):
		if 'admin' in request.META['PATH_INFO']:
			return {}
		else:
			list_ct = Institucion.objects.all()
			return {'list_cts': list_ct } 