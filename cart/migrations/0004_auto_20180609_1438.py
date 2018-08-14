# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-09 11:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_status',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='itemcart',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='itemcart',
            name='item',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='ItemCart',
        ),
    ]
