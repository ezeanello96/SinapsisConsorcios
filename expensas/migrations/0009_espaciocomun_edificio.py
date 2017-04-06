# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0008_auto_20161111_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='espaciocomun',
            name='edificio',
            field=models.ForeignKey(blank=True, to='expensas.Edificio', null=True),
        ),
    ]
