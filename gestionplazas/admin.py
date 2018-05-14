from django.contrib import admin

from .models import TiposEvaluacion, Evaluacion, Plaza, TiposNombramiento, Asignacion
admin.site.register(TiposEvaluacion)
admin.site.register(Evaluacion)
admin.site.register(Plaza)
admin.site.register(TiposNombramiento)
admin.site.register(Asignacion)