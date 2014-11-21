# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mainapp.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20141120_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='displayname',
            field=mainapp.utils.fields.RegexField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.member_file_name),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture1',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture2',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture3',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture4',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture5',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name),
        ),
    ]
