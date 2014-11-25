# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_auto_20141124_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='transaction',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.AddField(
            model_name='transaction',
            name='card',
            field=models.ForeignKey(default=0, to='mainapp.CreditCard'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='comment',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='critical',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
