# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-11 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chop', '0006_auto_20171108_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='receipt_images/'),
        ),
    ]
