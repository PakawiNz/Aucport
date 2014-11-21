# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mainapp.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20141120_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birthdate',
            field=mainapp.utils.fields.BirthdateField(),
        ),
    ]
