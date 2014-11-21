# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20141121_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='lastbid',
            field=models.DateTimeField(),
        ),
    ]
