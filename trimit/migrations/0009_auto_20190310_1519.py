# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-10 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trimit', '0008_auto_20190310_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='mean_atmosphere_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='mean_price_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='mean_service_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
