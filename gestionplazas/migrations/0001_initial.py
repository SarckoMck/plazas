# Generated by Django 2.0.5 on 2018-05-03 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestiondocentes', '0001_initial'),
        ('gestioncts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(max_length=10, verbose_name='Folio de registro')),
                ('fecha_asignacion', models.DateField(verbose_name='Fecha de asignacion')),
                ('desde', models.DateField(verbose_name='Fecha de Inicio')),
                ('hasta', models.DateField(verbose_name='Fecha de Fin')),
                ('cct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioncts.Institucion', verbose_name='Centro de trabajo')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('folio_concurso', models.CharField(default='', max_length=12, verbose_name='Folio Asignado')),
                ('resultado', models.CharField(choices=[('ID', 'Ideoneo'), ('NI', 'No ideoneo')], default='', max_length=2, verbose_name='Resultado Obtenido')),
                ('lista', models.CharField(default='', max_length=5, verbose_name='Número de lista')),
                ('prelacion', models.CharField(default='', max_length=4, verbose_name='Prelación Examen')),
                ('suestado', models.CharField(choices=[('ASI', 'Asignado'), ('BAJ', 'Baja'), ('PAS', 'Para asignar')], max_length=3, verbose_name='Estado Evalucación')),
                ('motivobaja', models.CharField(default='', max_length=20, verbose_name='Motivo de la baja')),
                ('curp_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestiondocentes.Docente')),
            ],
        ),
        migrations.CreateModel(
            name='Plaza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave_plaza', models.CharField(max_length=20, verbose_name='Clave de la plaza')),
                ('nivel_educ', models.CharField(choices=[('01', 'Educ. Inicial'), ('02', 'Educ. Preescolar'), ('03', 'Educ. Preescolar Indigena'), ('04', 'Educ. Primaria'), ('05', 'Educ. Primaria Indigena'), ('06', 'Educ. Secundaria'), ('07', 'Educ. Telesecundaria'), ('08', 'Educ. Secundaria Técnica'), ('09', 'Educ. Especial'), ('10', 'Educ. Media Superior'), ('11', 'Educ. Superior')], max_length=2, verbose_name='Nivel Educativo')),
                ('tipo_tramite', models.CharField(max_length=20, verbose_name='Tipo de tipo_tramite')),
                ('tipo_plaza', models.CharField(max_length=20, verbose_name='Tipo de Plaza')),
            ],
        ),
        migrations.CreateModel(
            name='TiposEvaluacion',
            fields=[
                ('id_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_reval', models.CharField(max_length=75, verbose_name='Tipo de evaluación')),
                ('destinario', models.CharField(choices=[('DOC', 'Docente'), ('TEC', 'Tecnico Docente')], default='DOC', max_length=3, verbose_name='Para')),
                ('nivel_esc', models.CharField(choices=[('01', 'Inicial y Preescolar'), ('02', 'Primaria'), ('03', 'Educación Indígena'), ('04', 'Inicial y Preescolar'), ('05', 'Edicación Especial'), ('06', 'Edución  Física'), ('07', 'Telesecundarias'), ('08', 'Secundarias Generales'), ('09', 'Extra Escolar')], default='01', max_length=2, verbose_name='Nivel escolar')),
            ],
        ),
        migrations.CreateModel(
            name='TiposNombramiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_nomb', models.CharField(max_length=75, verbose_name='Descripcion del nombramiento')),
            ],
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='tipo_eval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionplazas.TiposEvaluacion', verbose_name='Tipo de Evaluación'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='clave_plaza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionplazas.Plaza', verbose_name='Clave de la plaza'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='curp_doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestiondocentes.Docente', verbose_name='CURP del docentes'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='tipo_nombramiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionplazas.TiposNombramiento', verbose_name='Nombramiento'),
        ),
    ]
