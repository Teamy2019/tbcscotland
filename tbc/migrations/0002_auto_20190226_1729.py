# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-26 17:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tbc', '0001_initial'),
    ]

    operations = [
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
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tbc.Profile')),
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
        migrations.RemoveField(
            model_name='ad',
            name='category',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='profile',
        ),
        migrations.RenameField(
            model_name='inbox',
            old_name='sender',
            new_name='profile',
        ),
        migrations.RemoveField(
            model_name='inbox',
            name='ad',
        ),
        migrations.DeleteModel(
            name='Ad',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]