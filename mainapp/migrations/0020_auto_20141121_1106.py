# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_auto_20141121_0919'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_Category',
            new_name='Category',
        ),
    ]
