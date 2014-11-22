# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_auto_20141121_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='highest_auction',
            field=models.OneToOneField(related_name=b'highest_auction', null=True, blank=True, to='mainapp.Auction'),
            preserve_default=True,
        ),
    ]
