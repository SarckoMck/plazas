from django.db import models
from django.utils import timezone

class Docente(models.Model):
	
	EDOCIVIL_CHOICES = (
		('SOL', 'Soltero'),
		('CAS', 'Casado'),
		('UNI', 'Unión libre')
		)
	
	SEXO_CHOICES = (
		('M', 'Masculino'),
		('F', 'Femenino'),
		)
	
	apaterno = models.CharField(max_length=15, default="", verbose_name='Apellido Paterno')
	amaterno = models.CharField(max_length=15, default="", verbose_name='Apellido Materno')
	nombre = models.CharField(max_length=30, default="", verbose_name='Nombre del Docente')
	rfc = models.CharField(max_length=13, default="", verbose_name='RFC del docente')
	curp = models.CharField(max_length=18, primary_key=True, verbose_name='CURP del Docente')
	edo_civil = models.CharField(max_length=3, choices=EDOCIVIL_CHOICES, verbose_name='Estado Civil')
	sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo')
	dom_calle = models.CharField(max_length=50,default="",verbose_name='Calle y número')
	colonia = models.CharField(max_length=25, default="", verbose_name='Colonia')
	cp = models.CharField(max_length=5, default="", verbose_name='Codigo Postal')
	localidad = models.CharField(max_length=25, default="", verbose_name='Localidad')
	municipio = models.CharField(max_length=25, default="", verbose_name='Municipio')
	tel_cel = models.CharField(max_length=10, default="", verbose_name='Telefono Celular')
	e_mail = models.EmailField(max_length=254, verbose_name='Correo Electronico')
	
	def __str__(self):
		name_docente = self.nombre + ' ' + self.apaterno + ' ' + self.amaterno
		return name_docente