# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 10:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20171126_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='song_comment',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user_comment',
        ),
        migrations.DeleteModel(
            name='comments',
        ),
    ]