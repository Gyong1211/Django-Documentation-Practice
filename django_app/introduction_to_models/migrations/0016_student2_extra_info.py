# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0015_auto_20170607_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='student2',
            name='extra_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extra_students', to='introduction_to_models.CommonInfo2'),
        ),
    ]
