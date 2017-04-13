# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expensa',
            options={'ordering': ('fecha',), 'verbose_name': 'Expensa', 'verbose_name_plural': 'Expensas'},
        ),
        migrations.AlterField(
            model_name='expensa',
            name='archivo',
            field=models.FileField(upload_to=b'expensas/', verbose_name=b'Archivo'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='direccion',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Direcci\xc3\xb3n', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=30, null=True, verbose_name=b'Tel\xc3\xa9fono', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono2',
            field=models.CharField(max_length=30, null=True, verbose_name=b'Tel\xc3\xa9fono 2', blank=True),
        ),
        migrations.AlterField(
            model_name='rendicioncuenta',
            name='archivo',
            field=models.FileField(upload_to=b'informes/', verbose_name=b'Archivo'),
        ),
    ]
