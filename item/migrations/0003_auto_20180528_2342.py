# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-28 20:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item_item_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcomment',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='itemcomment',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='itemcomment',
            name='rating',
        ),
    ]