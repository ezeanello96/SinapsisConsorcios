# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0028_expensa_gasto'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasto',
            name='periodo',
            field=models.CharField(max_length=20, verbose_name=b'Periodo', blank=True),
        ),
    ]
