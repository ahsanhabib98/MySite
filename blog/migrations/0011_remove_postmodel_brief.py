# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-02 22:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_postmodel_photo2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='brief',
        ),
    ]
