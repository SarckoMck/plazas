# Generated by Django 2.0.5 on 2018-05-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondocentes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='curp',
            field=models.CharField(max_length=18, primary_key=True, serialize=False, verbose_name='CURP del Docente'),
        ),
    ]
