# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
    ]
