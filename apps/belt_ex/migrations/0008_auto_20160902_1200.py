# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_ex', '0007_auto_20160822_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_relate', to='belt_ex.User'),
        ),
    ]
