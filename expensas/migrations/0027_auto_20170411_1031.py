# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0026_auto_20170406_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificio',
            name='fondoDeReserva',
            field=models.FloatField(null=True, verbose_name=b'Fondo de Reserva', blank=True),
        ),
    ]
