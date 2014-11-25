# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_auto_20141125_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='auction',
            name='product',
            field=models.ForeignKey(related_name=b'auctions', to='mainapp.Product'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='product',
            field=models.ForeignKey(related_name=b'transactions', to='mainapp.Product'),
        ),
    ]
