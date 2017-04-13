# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0025_auto_20170323_0933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='edificio',
            options={'ordering': ('nombre',), 'verbose_name': 'Edificio / Consorcio', 'verbose_name_plural': 'Edificios / Consorcios'},
        ),
        migrations.AddField(
            model_name='edificio',
            name='fondoDeReserva',
            field=models.FloatField(default=0, verbose_name=b'Fondo de Reserva', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='edificios',
            field=models.ManyToManyField(to='expensas.Edificio'),
        ),
    ]
