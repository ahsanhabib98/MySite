# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-17 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postmodel_brief'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='active',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='read_time',
            field=models.IntegerField(default=0),
        ),
    ]