# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0017_numeroutil_servicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoImportante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('archivo', models.FileField(upload_to=b'importantes/', null=True, verbose_name=b'Archivo', blank=True)),
                ('fecha', models.DateField(auto_now_add=True, verbose_name=b'Fecha de subida')),
                ('edificio', models.ForeignKey(to='expensas.Edificio')),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Archivo importante',
                'verbose_name_plural': 'Archivos importantes',
            },
        ),
    ]
