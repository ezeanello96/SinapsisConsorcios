# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0019_tipodeunidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipodeGastos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('porcentajeA', models.IntegerField(verbose_name=b'Porcentaje A')),
                ('porcentajeB', models.IntegerField(verbose_name=b'Porcentaje B')),
                ('porcentajeC', models.IntegerField(verbose_name=b'Porcentaje C')),
                ('porcentajeD', models.IntegerField(verbose_name=b'Porcentaje D')),
                ('edificio', models.ForeignKey(to='expensas.Edificio')),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Tipo de Gastos',
                'verbose_name_plural': 'Tipos de Gastos',
            },
        ),
    ]
