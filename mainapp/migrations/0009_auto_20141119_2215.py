# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20141119_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture1',
            field=models.FileField(null=True, upload_to=mainapp.utils.fields.product_file_name),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='picture2',
            field=models.FileField(null=True, upload_to=mainapp.utils.fields.product_file_name),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='picture3',
            field=models.FileField(null=True, upload_to=mainapp.utils.fields.product_file_name),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='picture4',
            field=models.FileField(null=True, upload_to=mainapp.utils.fields.product_file_name),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='picture5',
            field=models.FileField(null=True, upload_to=mainapp.utils.fields.product_file_name),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='birthdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='confirmation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.FileField(null=True, upload_to=mainapp.utils.fields.member_file_name),
        ),
    ]
