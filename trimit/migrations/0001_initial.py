# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-12 18:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import tagulous.models.fields
import tagulous.models.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('flat_number', models.CharField(blank=True, max_length=15)),
                ('street_address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('postcode', models.CharField(blank=True, max_length=30)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('opening_times', models.CharField(blank=True, max_length=200, null=True)),
                ('webpage', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('profile_picture', models.ImageField(blank=True, default='DefaultPagePic.png', upload_to='user_profile_images')),
                ('contact_number', models.CharField(blank=True, max_length=15)),
                ('latitude', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=9, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hairpage_images')),
                ('text', models.CharField(blank=True, max_length=140)),
                ('upload_time', models.DateTimeField(null=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='trimit.Page')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_rating', models.DecimalField(decimal_places=1, default=0, max_digits=10)),
                ('atmosphere_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('price_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('service_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('picture', models.ImageField(blank=True, upload_to='review_images')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='trimit.Page')),
            ],
        ),
        migrations.CreateModel(
            name='Specialities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='UserHairImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user_hair_images')),
                ('text', models.CharField(blank=True, max_length=140)),
                ('upload_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, default='DefaultUserPic.png', upload_to='user_profile_images')),
                ('favourites', models.ManyToManyField(related_name='favourited', to='trimit.Page')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userhairimage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='trimit.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='specialities',
            unique_together=set([('slug',)]),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='trimit.UserProfile'),
        ),
        migrations.AddField(
            model_name='page',
            name='specialities',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, force_lowercase=True, help_text='Enter a comma-separated tag string', space_delimiter=False, to='trimit.Specialities', verbose_name_plural='Specialities', verbose_name_singular='Speciality'),
        ),
        migrations.AddField(
            model_name='page',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Page', to=settings.AUTH_USER_MODEL),
        ),
    ]
