# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 10:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab6_dj', '0004_auto_20161118_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_model',
            name='ante_for',
        ),
    ]
