# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0012_auto_20160625_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='content',
            field=models.CharField(blank=True, default='', max_length=512, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='rtype',
            field=models.CharField(choices=[('Video', 'Video'), ('Written Resource', 'Written Resource'), ('Slides', 'Slides'), ('External Resource', 'External Resource'), ('AP CS Principles Standards Mapping', 'AP CS Principles Standards Mapping'), ('CSTA Standards Mapping', 'CSTA Standards Mapping'), ('Programming Problem', 'Programming Problem'), ('Written Problem', 'Written Problem'), ('Teaching Tip', 'Teaching Tip'), ('Demonstration Idea', 'Demonstration Idea'), ('Thought Question', 'Thought Question'), ('Quiz Bank Link', 'Quiz Bank Link')], default='Video', max_length=5, verbose_name='resource type'),
        ),
    ]