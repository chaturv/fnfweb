# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0006_auto_20170513_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPoller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_ts', models.DateTimeField()),
                ('message_snippet', models.CharField(max_length=2048)),
                ('message_raw', models.TextField()),
                ('is_captured', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-received_ts'],
                'db_table': 'order_poller',
            },
        ),
    ]
