# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-30 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_remove_order_items_in_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]