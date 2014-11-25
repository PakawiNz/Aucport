# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mainapp.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_auto_20141125_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='cardid',
            field=mainapp.utils.fields.RegexField(default='', max_length=16),
            preserve_default=False,
        ),
    ]
