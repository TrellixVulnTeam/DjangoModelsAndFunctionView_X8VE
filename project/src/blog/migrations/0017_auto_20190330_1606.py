# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-03-30 20:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190330_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 30, 20, 6, 4, 693169, tzinfo=utc)),
        ),
    ]