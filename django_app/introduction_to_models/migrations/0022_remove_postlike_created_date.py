# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 03:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0021_auto_20170608_0323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postlike',
            name='created_date',
        ),
    ]
