# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_ex', '0005_auto_20160819_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='friend_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_relate', to='belt_ex.User'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_relate', to='belt_ex.User'),
        ),
    ]