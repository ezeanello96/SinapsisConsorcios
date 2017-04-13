# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0010_auto_20161111_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='hora',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name=b'Hora', choices=[(b'00', b'00'), (b'01', b'01')]),
        ),
    ]
