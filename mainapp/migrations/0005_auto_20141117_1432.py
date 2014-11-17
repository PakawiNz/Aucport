# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_member_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='confirmation',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='displayname',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
