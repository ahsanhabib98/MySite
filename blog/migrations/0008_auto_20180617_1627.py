# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-17 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180617_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='blog_image'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='blog_image'),
        ),
    ]
