# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab4', '0005_voltagesample_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='voltagesample',
            name='freq',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='voltagesample',
            name='raw',
            field=models.BooleanField(default=False),
        ),
    ]
