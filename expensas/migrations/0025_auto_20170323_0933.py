# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0024_persona_edificios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='edificios',
            field=models.ManyToManyField(to='expensas.Edificio', null=True, blank=True),
        ),
    ]
