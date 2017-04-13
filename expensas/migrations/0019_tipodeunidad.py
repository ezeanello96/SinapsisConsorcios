# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0018_archivoimportante'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipodeUnidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('edificio', models.ForeignKey(to='expensas.Edificio')),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Tipo de Unidad',
                'verbose_name_plural': 'Tipos de Unidades',
            },
        ),
    ]
