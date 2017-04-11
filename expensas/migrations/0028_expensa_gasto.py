# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0027_auto_20170411_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expensa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=20, verbose_name=b'Tipo de expensa')),
                ('periodo', models.CharField(max_length=20, verbose_name=b'Periodo')),
                ('total', models.FloatField(verbose_name=b'Total')),
                ('edificio', models.ForeignKey(to='expensas.Edificio')),
            ],
            options={
                'ordering': ('edificio', 'periodo'),
                'verbose_name': 'Expensa',
                'verbose_name_plural': 'Expensas',
            },
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(verbose_name=b'Fecha del gasto')),
                ('importe', models.FloatField(verbose_name=b'Importe')),
                ('descripcion', models.CharField(max_length=50, verbose_name=b'Descripci\xc3\xb3n')),
                ('factura', models.FileField(upload_to=b'gastos/', verbose_name=b'Archivo')),
                ('expensa', models.ForeignKey(to='expensas.Expensa')),
                ('tipoDeGasto', models.ForeignKey(to='expensas.TipodeGastos')),
            ],
            options={
                'ordering': ('fecha', 'tipoDeGasto'),
                'verbose_name': 'Gasto',
                'verbose_name_plural': 'Gastos',
            },
        ),
    ]
