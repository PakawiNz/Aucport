# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mainapp.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_product_highest_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='current',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='auction',
            name='lastbid',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.member_file_name, blank=True),
        ),
    ]
