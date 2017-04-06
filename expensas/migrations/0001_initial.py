# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('piso', models.CharField(max_length=2, verbose_name=b'Piso')),
                ('departamento', models.CharField(max_length=2, verbose_name=b'Departamento')),
            ],
            options={
                'ordering': ('edificio', 'piso', 'departamento'),
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre del Edificio')),
                ('direccion', models.CharField(max_length=50, verbose_name=b'Direcci\xc3\xb3n')),
                ('observaciones', models.CharField(max_length=250, verbose_name=b'Observaciones')),
            ],
            options={
                'ordering': ('nombre',),
                'verbose_name': 'Edificio',
                'verbose_name_plural': 'Edificios',
            },
        ),
        migrations.CreateModel(
            name='Expensa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True, verbose_name=b'Fecha')),
                ('archivo', models.FileField(upload_to=b'', verbose_name=b'Archivo')),
                ('dpto', models.ForeignKey(to='expensas.Departamento')),
            ],
            options={
                'ordering': ('fecha',),
                'verbose_name': 'Rendici\xf3n de Cuenta',
                'verbose_name_plural': 'Rendiciones de Cuenta',
            },
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True, verbose_name=b'Fecha')),
                ('mensaje', models.CharField(max_length=1000, verbose_name=b'Mensaje')),
                ('fechaLeido', models.DateField(default=None, null=True, verbose_name=b'Fecha Le\xc3\xaddo', blank=True)),
            ],
            options={
                'ordering': ('fecha',),
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefono', models.CharField(max_length=30, verbose_name=b'Tel\xc3\xa9fono')),
                ('telefono2', models.CharField(max_length=30, verbose_name=b'Tel\xc3\xa9fono 2')),
                ('direccion', models.CharField(max_length=50, verbose_name=b'Direcci\xc3\xb3n')),
            ],
            options={
                'ordering': ('last_name', 'first_name'),
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='RendicionCuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True, verbose_name=b'Fecha')),
                ('archivo', models.FileField(upload_to=b'', verbose_name=b'Archivo')),
                ('edificio', models.ForeignKey(to='expensas.Edificio')),
            ],
            options={
                'ordering': ('fecha',),
                'verbose_name': 'Rendici\xf3n de Cuenta',
                'verbose_name_plural': 'Rendiciones de Cuenta',
            },
        ),
        migrations.AddField(
            model_name='mensaje',
            name='desde',
            field=models.ForeignKey(related_name='Remitente', to='expensas.Persona'),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='para',
            field=models.ForeignKey(related_name='Destinatario', to='expensas.Persona'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='edificio',
            field=models.ForeignKey(to='expensas.Edificio'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='inquilino',
            field=models.ForeignKey(related_name='Inquilino', to='expensas.Persona', null=True),
        ),
        migrations.AddField(
            model_name='departamento',
            name='propietario',
            field=models.ForeignKey(related_name='Propietario', to='expensas.Persona'),
        ),
    ]
