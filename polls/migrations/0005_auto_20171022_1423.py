# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20171013_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='publish_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='date published'),
        ),
    ]
