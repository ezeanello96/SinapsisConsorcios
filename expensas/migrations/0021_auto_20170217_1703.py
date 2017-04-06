# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0020_tipodegastos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ph', models.CharField(max_length=4, verbose_name=b'PH')),
                ('depto', models.CharField(max_length=5, verbose_name=b'Depto')),
                ('porcentual', models.FloatField(verbose_name=b'Porcentual (%)')),
                ('edificio', models.ForeignKey(to='expensas.Edificio')),
                ('inquilino', models.ForeignKey(related_name='Inquilino', blank=True, to='expensas.Persona', null=True)),
                ('propietario', models.ForeignKey(related_name='Propietario', to='expensas.Persona')),
                ('tipodeunidad', models.ForeignKey(to='expensas.TipodeUnidad')),
            ],
            options={
                'ordering': ('edificio', 'ph', 'tipodeunidad'),
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
        ),
        migrations.RemoveField(
            model_name='departamento',
            name='edificio',
        ),
        migrations.RemoveField(
            model_name='departamento',
            name='inquilino',
        ),
        migrations.RemoveField(
            model_name='departamento',
            name='propietario',
        ),
        migrations.RemoveField(
            model_name='expensa',
            name='dpto',
        ),
        migrations.RemoveField(
            model_name='expensa',
            name='rendicion',
        ),
        migrations.DeleteModel(
            name='Departamento',
        ),
        migrations.DeleteModel(
            name='Expensa',
        ),
    ]
