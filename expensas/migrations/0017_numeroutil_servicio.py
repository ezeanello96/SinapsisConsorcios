# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0016_numeroutil'),
    ]

    operations = [
        migrations.AddField(
            model_name='numeroutil',
            name='servicio',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Servicio', blank=True),
        ),
    ]
