from django.db import models

class Institucion(models.Model):
	
	TURNO_CHOICES = (
        ('100', 'Matutino'),
        ('120', 'Matutino y Vespertino'),
        ('200', 'Vespertino'),
        ('600', 'Complementario'),
        ('700', 'Continuo (Jornada amplía)'),
        )
	
	AMEAL = '001'
	PINAL = '002'
	ASECO = '003'
	CADER = '004'
	COLON = '005'
	CORRE = '006'
	EMONT = '007'
	HUIMI = '008'
	JALPA = '009'
	LANDA = '010'
	MARQU = '011'
	PEDRO = '012'
	PENAM = '013'
	QUERE = '014'
	SANJO = '015'
	SANJU = '016'
	TEQUI = '017'
	TOLIM = '018'	
	
	MUNICIPIOS_QRO = (
		(AMEAL, 'Amealco de Bonfil'),
		(PINAL, 'Pinal de Amoles'),
		(ASECO, 'Arroyo Seco'),
		(CADER, 'Caderyta'),
		(COLON, 'Colon'),
		(EMONT, 'Ezequiel Montes'),
		(HUIMI, 'Huimilpan'),
		(JALPA, 'Jalpan de Serra'),
		(LANDA, 'Landa de Matamoros'),
		(MARQU, 'El Maqués'),
		(PEDRO, 'Pedro Escobedo'),
		(PENAM, 'Peñamiller'),
		(QUERE, 'Querétaro de Arteaga'),
		(SANJO, 'San Joaquín'),
		(SANJU, 'San Juan del Rio'),
		(TEQUI, 'Tequisquiapan'),
		(TOLIM, 'Toliman'),
		)
	
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
		
	ESTADOS_MEXICO = (
		('01','Aguascalientes'),
		('02','Baja California'),
		('03','Baja California Sur'),
		('04','Campeche'),
		('05','Coahuila de Zaragoza'),
		('06','Colima'),
		('07','Chiapas'),
		('08','Chihuahua'),
		('09','Ciudad de México'),
		('10','Durango'),
		('11','Guanajuato'),
		('12','Guerrero'),
		('13','Hidalgo'),
		('14','Jalisco'),
		('15','México'),
		('16','Michoacán de Ocampo'),
		('17','Morelos'),
		('18','Nayarit'),
		('19','Nuevo León'),
		('20','Oaxaca'),
		('21','Puebla'),
		('22','Querétaro'),
		('23','Quintana Roo'),
		('24','San Luis Potosí'),
		('25','Sinaloa'),
		('26','Sonora'),
		('27','Tabasco'),
		('28','Tamaulipas'),
		('29','Tlaxcala'),
		('30','Veracruz de Ignacio de la Llave'),
		('31','Yucatán'),
		('32','Zacatecas'),
	)
	
	clave_ct = models.CharField(primary_key=True, max_length=10, verbose_name='Clave del Centro de trabajo')
	nombre_ct = models.CharField(max_length=25, default="", verbose_name='Nombre de la Escuela')
	nivel_educ = models.CharField(max_length=2, choices=NIVEL_EDUCATIVO, verbose_name='Nivel Educativo')
	turno = models.CharField(max_length=3, choices=TURNO_CHOICES, default="100",verbose_name='Turno')
	zona_esc = models.CharField(max_length=2, default="", verbose_name='Zona Escolar')
	sector = models.CharField(max_length=2, default="", verbose_name='Sector Educativo')
	dom_calle = models.CharField(max_length=50,default="",verbose_name='Calle y número')
	cp = models.CharField(max_length=5, default="", verbose_name='Codigo Postal')
	municipio = models.CharField(max_length=3, choices=MUNICIPIOS_QRO, verbose_name='Municipio')
	estado = models.CharField(max_length=2, choices=ESTADOS_MEXICO, default="22", verbose_name='Estado')
	
	def __str__(self):
		escuela = self.clave_ct + ' - ' + self.nombre_ct
		return escuela