# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0012_auto_20161111_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='hora',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Hora', choices=[(0, b'00'), (1, b'01'), (2, b'02'), (3, b'03'), (4, b'04'), (5, b'05'), (6, b'06'), (7, b'07'), (8, b'08'), (9, b'09'), (10, b'10'), (11, b'11'), (12, b'12'), (13, b'13'), (14, b'14'), (15, b'15'), (16, b'16'), (17, b'17'), (18, b'18'), (19, b'19'), (20, b'20'), (21, b'21'), (22, b'22'), (23, b'23'), (24, b'24')]),
        ),
    ]
