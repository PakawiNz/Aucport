# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mainapp.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20141121_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', mainapp.utils.fields.CharField(max_length=80)),
                ('parent', models.ForeignKey(related_name=b'children', blank=True, to='mainapp.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='capacity',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=0, to='mainapp.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='defection',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='dimension',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_condition',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='properties',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='selling_condition',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_condition',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='version',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='picture1',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture2',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture3',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture4',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture5',
            field=models.ImageField(null=True, upload_to=mainapp.utils.fields.product_file_name, blank=True),
        ),
    ]
