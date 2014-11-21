# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20141121_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='lastbid',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 21, 13, 14, 10, 471000)),
        ),
    ]
