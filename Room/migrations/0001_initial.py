# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-28 13:03
from __future__ import unicode_literals

import Account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField(default=8000, unique=True)),
                ('title', models.CharField(default='Default room title', max_length=200)),
                ('description', models.CharField(default='Default description for a default room', max_length=1000)),
                ('state', models.BooleanField(default=False)),
                ('interviewees', models.ManyToManyField(to='Account.Interviewee')),
                ('interviewer', models.OneToOneField(default=Account.models.Interviewer(), on_delete=django.db.models.deletion.CASCADE, to='Account.Interviewer')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
