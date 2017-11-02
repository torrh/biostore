# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_producer_farmurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='latitude',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='producer',
            name='longitude',
            field=models.CharField(default='0.0.0', max_length=255),
        ),
        migrations.AlterField(
            model_name='producer',
            name='phone_number',
            field=models.CharField(default='0.0.0', max_length=255),
        ),
    ]
