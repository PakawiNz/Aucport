# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20141121_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='lastbid',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 21, 13, 14, 0, 655000)),
        ),
    ]
