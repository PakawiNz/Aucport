# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mainapp.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20141119_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=mainapp.utils.fields.RegexField(max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='member',
            name='firstname',
            field=mainapp.utils.fields.AlphaNumericField(max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='lastname',
            field=mainapp.utils.fields.AlphaNumericField(max_length=50),
        ),
    ]
