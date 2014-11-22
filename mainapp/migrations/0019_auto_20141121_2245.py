# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_auto_20141121_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_condition',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='properties',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_condition',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='shipping_condition',
            field=models.TextField(null=True, blank=True),
        ),
    ]
