# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0029_gasto_periodo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasto',
            name='periodo',
        ),
    ]
