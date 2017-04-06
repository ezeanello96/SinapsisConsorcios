# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0004_auto_20160729_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='asunto',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Asunto'),
        ),
    ]
