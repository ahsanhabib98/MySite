# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180526_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='brief',
            field=models.CharField(default='1', max_length=500),
            preserve_default=False,
        ),
    ]