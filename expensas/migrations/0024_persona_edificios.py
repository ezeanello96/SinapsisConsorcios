# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0023_auto_20170221_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='edificios',
            field=models.ManyToManyField(to='expensas.Edificio'),
        ),
    ]
