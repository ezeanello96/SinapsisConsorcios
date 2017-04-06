# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0009_espaciocomun_edificio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserva',
            options={'ordering': ('fecha',), 'verbose_name': 'Reserva', 'verbose_name_plural': 'Reservas'},
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='hora',
        ),
    ]
