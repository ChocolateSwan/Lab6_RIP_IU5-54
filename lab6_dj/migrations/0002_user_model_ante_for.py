# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab6_dj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_model',
            name='ante_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab6_dj.ante_model'),
        ),
    ]
