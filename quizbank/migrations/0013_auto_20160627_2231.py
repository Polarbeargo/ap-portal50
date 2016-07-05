# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizbank', '0012_auto_20160627_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='a_image',
            field=models.ImageField(blank=True, null=True, upload_to='quizbank/a/', verbose_name='Answer Image'),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_image',
            field=models.ImageField(blank=True, null=True, upload_to='quizbank/q/', verbose_name='Question Image'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qtype',
            field=models.CharField(choices=[('Multiple Choice', 'Multiple Choice'), ('Fill in the Blanks', 'Fill in the Blanks'), ('Short Answer', 'Short Answer'), ('Free Response', 'Free Response'), ('Code Response', 'Code'), ('True/False', 'True/False'), ('Matching', 'Matching'), ('Fill in the Table', 'Fill in the Table'), ('Other', 'Other')], default='Short Answer', max_length=50, verbose_name='question type'),
        ),
    ]
