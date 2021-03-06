# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-03 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='service_image')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
