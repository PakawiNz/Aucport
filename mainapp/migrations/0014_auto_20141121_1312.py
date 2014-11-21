# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mainapp.utils.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20141121_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='product',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='auction',
            name='bidder',
            field=models.ForeignKey(default=0, to='mainapp.Member'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auction',
            name='ceiling',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='auction',
            name='current',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auction',
            name='increase',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='auction',
            name='isAuto',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='auction',
            name='lastbid',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 21, 13, 11, 46, 298000)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='auction',
            name='notify',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedback',
            name='isReport',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedback',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=mainapp.utils.fields.RegexField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now(), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auction',
            name='product',
            field=models.ForeignKey(to='mainapp.Product'),
        ),
    ]
