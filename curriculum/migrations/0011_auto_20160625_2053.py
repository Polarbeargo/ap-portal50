# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0010_auto_20160625_1657'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={},
        ),
        migrations.AlterField(
            model_name='chapter',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='duration',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='module',
            name='duration',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='module',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='resource',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='resource',
            name='link',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
    ]
