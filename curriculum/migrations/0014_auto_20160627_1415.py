# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0013_auto_20160627_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcevisibility',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
