# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0004_chapter_chaptervisibility_module_modulevisibility_resource_resourcevisibility'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chaptervisibility',
            options={'verbose_name_plural': 'chapter visibilities'},
        ),
        migrations.AlterModelOptions(
            name='modulevisibility',
            options={'verbose_name_plural': 'module visibilities'},
        ),
        migrations.AlterModelOptions(
            name='resourcevisibility',
            options={'verbose_name_plural': 'resource visibilities'},
        ),
        migrations.AddField(
            model_name='module',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
