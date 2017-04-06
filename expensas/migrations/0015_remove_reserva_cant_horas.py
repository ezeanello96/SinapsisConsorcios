# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0014_auto_20161114_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='cant_horas',
        ),
    ]
