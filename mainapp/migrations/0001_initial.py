# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('displayname', models.CharField(max_length=50)),
                ('birthdate', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('netPrice', models.FloatField()),
                ('state', models.IntegerField(choices=[(1, b'pending'), (2, b'selling'), (3, b'auction'), (4, b'billing'), (6, b'soldout'), (5, b'abandoned')])),
                ('owner', models.ForeignKey(to='mainapp.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('buyer', models.ForeignKey(to='mainapp.Member')),
                ('product', models.ForeignKey(to='mainapp.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='feedback',
            name='transaction',
            field=models.ForeignKey(to='mainapp.Transaction'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creditcard',
            name='owner',
            field=models.ForeignKey(to='mainapp.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(to='mainapp.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='auction',
            name='product',
            field=models.OneToOneField(to='mainapp.Product'),
            preserve_default=True,
        ),
    ]
