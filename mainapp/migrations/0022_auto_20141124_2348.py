# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_auto_20141124_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='increase',
            field=models.FloatField(default=1),
        ),
    ]
