# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizbank', '0015_auto_20160629_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('position', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='qtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quizbank.QuestionType', verbose_name='question type'),
        ),
    ]
