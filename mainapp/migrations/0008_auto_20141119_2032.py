# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_member_isconfirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='picture',
            field=models.FileField(null=True, upload_to=b'profilepic/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='isConfirmed',
            field=models.BooleanField(default=False),
        ),
    ]
