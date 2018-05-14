from django.db import models 
from gestiondocentes.models import Docente
from gestioncts.models import Institucion

class TiposEvaluacion(models.Model):

	DESTINATARIO_CHOICES = (
		('DOC', 'Docente'),
		('TEC', 'Tecnico Docente'),
		)
	
	NIVELESESC_CHOICES = (
		('01','Inicial y Preescolar'),
		('02','Primaria'),
		('03','Educación Indígena'),
		('04','Inicial y Preescolar'),
		('05','Edicación Especial'),
		('06','Edución  Física'),
		('07','Telesecundarias'),
		('08','Secundarias Generales'),
		('09','Extra Escolar'),
		)
	
	id_tipo = models.AutoField(primary_key=True)
	descripcion_reval = models.CharField(max_length=75, verbose_name='Tipo de evaluación')
	destinario = models.CharField(max_length=3, choices=DESTINATARIO_CHOICES, default="DOC",verbose_name='Para')
	nivel_esc = models.CharField(max_length=2, choices=NIVELESESC_CHOICES, default="01",verbose_name='Nivel escolar')
	
	def __str__(self):
		return self.descripcion_reval


class Evaluacion(models.Model):
	
	EDO_EVALUACION = (
		('ASI', 'Asignado'),
		('BAJ', 'Baja'),
		('PAS', 'Para asignar'),
		)
	
	RESULTADO_EXA = (
		('ID', 'Ideoneo'),
		('NI', 'No ideoneo'),
		)
	
	id = models.AutoField(primary_key=True)
	folio_concurso = models.CharField(max_length=12, default="", verbose_name='Folio Asignado')
	
	curp_doc = models.ForeignKey(Docente, on_delete=models.CASCADE, verbose_name='Docente')
	
	tipo_eval = models.ForeignKey(TiposEvaluacion, on_delete=models.CASCADE, verbose_name='Tipo de Evaluación') 
	resultado = models.CharField(max_length=2, choices=RESULTADO_EXA, default="", verbose_name='Resultado Obtenido') 
	#lista = models.CharField(max_length=5, default="", verbose_name='Número de lista')
	lista = models.IntegerField(verbose_name='Número de lista')
	prelacion = models.IntegerField(verbose_name='Orden prelación')
	suestado = models.CharField(max_length=3, choices=EDO_EVALUACION, verbose_name='Estado Evaluación')
	motivobaja = models.CharField(max_length=20, default="", blank=True, verbose_name='Motivo de la baja')
	
	def __str__(self):
		docente_prelacion = str(self.prelacion) + " - " + str(self.curp_doc)
		return docente_prelacion

class Plaza(models.Model):

	NIVEL_EDUCATIVO = (
		('01','Educ. Inicial'),
		('02','Educ. Preescolar'),
		('03','Educ. Preescolar Indigena'),
		('04','Educ. Primaria'),
		('05','Educ. Primaria Indigena'),
		('06','Educ. Secundaria'),
		('07','Educ. Telesecundaria'),
		('08','Educ. Secundaria Técnica'),
		('09','Educ. Especial'),
		('10','Educ. Media Superior'),
		('11','Educ. Superior'),
		)

	clave_plaza = models.CharField(max_length=20, verbose_name='Clave de la plaza')
	nivel_educ = models.CharField(max_length=2, choices=NIVEL_EDUCATIVO,verbose_name='Nivel Educativo')
	tipo_tramite = models.CharField(max_length=20, verbose_name='Tipo de tipo_tramite')
	tipo_plaza = models.CharField(max_length=20, verbose_name='Tipo de Plaza')
	
	def __str__(self):
		return self.clave_plaza

class TiposNombramiento(models.Model):

	id = models.AutoField(primary_key=True)
	descripcion_nomb = models.CharField(max_length=75, verbose_name='Descripcion del nombramiento')

	def __str__(self):
		return self.descripcion_nomb
		

class Asignacion(models.Model):

	TIPOS_NOM_CHOICES = (
		('1','Provisional'),
		('2','Definitiva'),
		('3','Fija'),
		)

	folio = models.CharField(max_length=10, verbose_name='Folio de registro')
	fecha_asignacion = models.DateField(auto_now=False,auto_now_add=False,verbose_name='Fecha de asignacion' )
	
	clave_plaza = models.ForeignKey(Plaza, on_delete=models.CASCADE, verbose_name='Clave de la plaza')
	curp_doc = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, verbose_name='Docente')
	cct = models.ForeignKey(Institucion, on_delete=models.CASCADE, verbose_name='Centro de trabajo')

	tipo_nombramiento = models.ForeignKey(TiposNombramiento, on_delete=models.CASCADE, verbose_name='Nombramiento')
	desde = models.DateField(auto_now=False,auto_now_add=False,verbose_name='Fecha de Inicio')
	hasta = models.DateField(auto_now=False,auto_now_add=False,verbose_name='Fecha de Fin')

	def __str__(self):
		return self.folio + " : " + str(self.curp_doc)