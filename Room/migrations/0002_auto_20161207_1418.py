# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='manager',
        ),
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='room',
            name='state',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.CharField(default='room', max_length=200),
        ),
        migrations.AlterField(
            model_name='room',
            name='url',
            field=models.URLField(default='/room/usr/index'),
        ),
    ]
