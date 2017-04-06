# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0021_auto_20170217_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Porcentuales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gasto', models.CharField(max_length=2, verbose_name=b'Gasto')),
                ('porcentual', models.FloatField(verbose_name=b'Porcentual (%)')),
                ('unidad', models.ForeignKey(to='expensas.Unidad')),
            ],
            options={
                'ordering': ('unidad', 'gasto'),
                'verbose_name': 'Porcentual',
                'verbose_name_plural': 'Porcentuales',
            },
        ),
    ]
