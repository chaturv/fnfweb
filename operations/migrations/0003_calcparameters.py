# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_auto_20170509_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalcParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'calc_parameters',
                'verbose_name': 'Calculation Parameter',
                'verbose_name_plural': 'Calculation Parameters',
            },
        ),
    ]
