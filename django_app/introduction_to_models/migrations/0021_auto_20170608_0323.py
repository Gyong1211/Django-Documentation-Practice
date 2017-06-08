# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0020_auto_20170608_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'introduction_to_models_post_like_users',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='like_users',
            field=models.ManyToManyField(related_name='like_posts', through='introduction_to_models.PostLike', to='introduction_to_models.User'),
        ),
        migrations.AddField(
            model_name='postlike',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='introduction_to_models.Post'),
        ),
        migrations.AddField(
            model_name='postlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='introduction_to_models.User'),
        ),
    ]
