# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-16 03:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0011_auto_20180515_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 3, 9, 53, 371893, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 3, 9, 53, 371392, tzinfo=utc)),
        ),
    ]