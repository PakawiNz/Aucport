# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_creditcard_cardid'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='unwatched',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='state',
            field=models.IntegerField(choices=[(1, b'pending'), (2, b'selling'), (3, b'auction'), (4, b'billing'), (6, b'soldout'), (5, b'abandon')]),
        ),
    ]
