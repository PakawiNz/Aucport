# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mainapp.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20141121_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture1',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='picture2',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='picture3',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='picture4',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='picture5',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name, blank=True),
            preserve_default=True,
        ),
    ]
