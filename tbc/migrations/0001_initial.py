# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-13 12:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LendAndSell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, upload_to='LendAndSell_images')),
                ('price', models.CharField(max_length=128)),
                ('availability', models.CharField(max_length=128)),
                ('keywords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('image', models.ImageField(blank=True, upload_to='profile_images')),
                ('skills', models.TextField()),
                ('education', models.TextField()),
                ('aboutme', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('portfolio', models.ImageField(blank=True, upload_to='portfolio_images')),
                ('activities', models.ImageField(blank=True, upload_to='activities_images')),
                ('views', models.IntegerField(default=0)),
                ('reviews', models.TextField()),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('lookingFor', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, upload_to='Projects_images')),
                ('timeline', models.CharField(max_length=128)),
                ('keywords', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tbc.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, upload_to='Service_images')),
                ('price', models.CharField(max_length=128)),
                ('availability', models.CharField(max_length=128)),
                ('keywords', models.TextField()),
                ('location', models.CharField(max_length=128)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tbc.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lendandsell',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tbc.Profile'),
        ),
        migrations.AddField(
            model_name='inbox',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tbc.Profile'),
        ),
    ]
