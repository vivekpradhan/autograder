# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign5', '0003_submission_assignment_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='password',
            field=models.CharField(default='', max_length=10),
        ),
    ]
