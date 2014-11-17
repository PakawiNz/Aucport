# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20141109_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='confirmation',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
