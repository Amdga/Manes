# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-10 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trimit', '0009_auto_20190310_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='average_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
    ]
