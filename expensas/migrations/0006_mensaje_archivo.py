# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0005_mensaje_asunto'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='archivo',
            field=models.FileField(upload_to=b'adjuntos/', null=True, verbose_name=b'Archivo Adjunto'),
        ),
    ]
