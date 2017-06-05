# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0003_auto_20170605_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_type',
            field=models.CharField(choices=[('students', '학생'), ('teacher', '선생')], default='students', max_length=10, verbose_name='유형'),
        ),
        migrations.AddField(
            model_name='person',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='introduction_to_models.Person'),
        ),
    ]