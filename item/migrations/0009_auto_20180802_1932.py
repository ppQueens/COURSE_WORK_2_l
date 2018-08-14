# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-02 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_itemfield_use_as_customer_filter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemfield',
            name='use_as_customer_filter',
        ),
        migrations.AddField(
            model_name='itemfielditem',
            name='use_as_customer_filter',
            field=models.BooleanField(default=None),
        ),
    ]
