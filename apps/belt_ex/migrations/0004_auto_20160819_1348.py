# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 20:48
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('belt_ex', '0003_auto_20160819_1334'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='relationship',
            managers=[
                ('relate', django.db.models.manager.Manager()),
            ],
        ),
    ]
