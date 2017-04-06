# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0022_porcentuales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porcentuales',
            name='gasto',
            field=models.CharField(max_length=1, verbose_name=b'Gasto'),
        ),
    ]
