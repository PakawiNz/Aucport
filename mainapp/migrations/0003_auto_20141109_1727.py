# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_timezone'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='timezone',
            field=models.ForeignKey(default=0, to='mainapp.Timezone'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='country',
            field=models.ForeignKey(to='mainapp.Country'),
        ),
    ]
