# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 13:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0016_auto_20161223_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='outdate_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 23, 21, 15, 56, 244724)),
        ),
    ]
