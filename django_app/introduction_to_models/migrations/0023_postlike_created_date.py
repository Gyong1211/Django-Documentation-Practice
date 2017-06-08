# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 03:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0022_remove_postlike_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='postlike',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]