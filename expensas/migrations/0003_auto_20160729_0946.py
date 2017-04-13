# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0002_auto_20160728_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='inquilino',
            field=models.ForeignKey(related_name='Inquilino', blank=True, to='expensas.Persona', null=True),
        ),
        migrations.AlterField(
            model_name='edificio',
            name='observaciones',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Observaciones', blank=True),
        ),
    ]
