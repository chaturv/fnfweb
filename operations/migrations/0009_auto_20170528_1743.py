# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-28 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0008_orderpoller_message_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery',
        ),
        migrations.AddField(
            model_name='deliveryinfo',
            name='order',
            field=models.ForeignKey(default=99, on_delete=django.db.models.deletion.CASCADE, to='operations.Order'),
            preserve_default=False,
        ),
    ]
