# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mainapp.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20141120_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=mainapp.utils.fields.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='confirmation',
            field=mainapp.utils.fields.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='displayname',
            field=mainapp.utils.fields.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='password',
            field=mainapp.utils.fields.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='timezone',
            name='name',
            field=mainapp.utils.fields.CharField(max_length=80),
        ),
    ]
