# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0007_orderpoller'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderpoller',
            name='message_id',
            field=models.CharField(default='m_id', max_length=50),
            preserve_default=False,
        ),
    ]
