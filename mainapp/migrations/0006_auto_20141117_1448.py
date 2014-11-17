# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20141117_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='confirmation',
            field=models.CharField(max_length=50),
        ),
    ]
