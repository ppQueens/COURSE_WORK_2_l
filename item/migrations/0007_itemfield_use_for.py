# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-02 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_auto_20180528_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemfield',
            name='use_for',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
