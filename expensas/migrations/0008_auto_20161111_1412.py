# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expensas', '0007_auto_20160801_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspacioComun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('descripcion', models.CharField(max_length=250, verbose_name=b'Descripcion')),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Espacio comun',
                'verbose_name_plural': 'Espacios comunes',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(verbose_name=b'Fecha')),
                ('hora', models.TimeField(verbose_name=b'Hora')),
                ('cant_horas', models.IntegerField(verbose_name=b'Cantidad de horas')),
                ('espacioComun', models.ForeignKey(to='expensas.EspacioComun')),
                ('persona', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('fecha', 'hora'),
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ('edificio', 'piso', 'departamento'), 'verbose_name': 'Departamento / Duplex', 'verbose_name_plural': 'Departamentos / Duplexs'},
        ),
        migrations.AlterModelOptions(
            name='edificio',
            options={'ordering': ('nombre',), 'verbose_name': 'Edificio / Complejo', 'verbose_name_plural': 'Edificios / Complejos'},
        ),
        migrations.AlterField(
            model_name='edificio',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name=b'Nombre'),
        ),
    ]
