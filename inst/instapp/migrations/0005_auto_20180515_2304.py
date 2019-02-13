# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-16 03:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0004_auto_20180515_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pulished_date',
            new_name='published_date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 3, 4, 29, 62846, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 3, 4, 29, 61843, tzinfo=utc)),
        ),
    ]
