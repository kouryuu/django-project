# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='passw_hash',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='demo', max_length=200),
            preserve_default=False,
        ),
    ]
