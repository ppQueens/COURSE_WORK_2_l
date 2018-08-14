# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-13 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='shipment_status',
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-update_date',)},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_create_date',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_update_date',
            new_name='update_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_payment',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_shipment',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_service',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Shipment',
        ),
    ]
