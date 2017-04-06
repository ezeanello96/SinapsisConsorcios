# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0015_remove_reserva_cant_horas'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumeroUtil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.IntegerField(verbose_name=b'Telefono')),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('edificio', models.ManyToManyField(to='expensas.Edificio')),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Numero Util',
                'verbose_name_plural': 'Numeros Utiles',
            },
        ),
    ]
