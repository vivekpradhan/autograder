# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign5', '0008_auto_20171008_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subresults',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subresults',
            name='events_sorted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subresults',
            name='features_sorted',
            field=models.BooleanField(default=False),
        ),
    ]
