# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0006_mensaje_archivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensa',
            name='rendicion',
            field=models.ForeignKey(blank=True, to='expensas.RendicionCuenta', null=True),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='archivo',
            field=models.FileField(upload_to=b'adjuntos/', null=True, verbose_name=b'Archivo Adjunto', blank=True),
        ),
    ]
