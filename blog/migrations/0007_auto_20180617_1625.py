# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-17 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180617_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='photo',
            field=models.ImageField(upload_to='blog_image'),
        ),
    ]
