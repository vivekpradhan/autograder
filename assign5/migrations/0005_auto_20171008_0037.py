# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign5', '0004_submission_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='eid',
            field=models.CharField(max_length=10),
        ),
    ]
