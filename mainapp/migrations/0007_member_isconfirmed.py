# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20141117_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='isConfirmed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
