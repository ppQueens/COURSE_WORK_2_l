# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-16 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(default=None, max_length=100)),
                ('description', models.TextField(blank=True, default=None)),
                ('brand_web_site', models.CharField(blank=True, default=None, max_length=70)),
            ],
            options={
                'db_table': 'brand',
            },
        ),
    ]
