# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-16 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
        ('customer', '0001_initial'),
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_add', models.DateTimeField(auto_now_add=True)),
                ('cart_status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='status.Status')),
                ('customer', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
            options={
                'verbose_name_plural': 'Cart',
                'db_table': 'Cart',
            },
        ),
        migrations.CreateModel(
            name='ItemCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_quantity', models.PositiveIntegerField(default=0)),
                ('cart', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
                ('item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='item.Item')),
            ],
            options={
                'verbose_name_plural': 'ItemCart',
                'db_table': 'ItemCart',
            },
        ),
    ]
