# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-10 00:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20180528_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_fl_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_login',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_phone',
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_type',
            field=models.IntegerField(blank=True, choices=[(0, 'made order'), (1, 'registered')], null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='fl_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.PositiveIntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='social_profile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
