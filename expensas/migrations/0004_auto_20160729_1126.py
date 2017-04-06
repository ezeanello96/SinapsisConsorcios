# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0003_auto_20160729_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='desde',
            field=models.ForeignKey(related_name='Remitente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='para',
            field=models.ForeignKey(related_name='Destinatario', to=settings.AUTH_USER_MODEL),
        ),
    ]
