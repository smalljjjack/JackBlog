# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-16 03:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0018_auto_20180515_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 3, 25, 31, 275746, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 3, 25, 31, 275746, tzinfo=utc)),
        ),
    ]
