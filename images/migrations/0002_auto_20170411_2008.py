# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-11 12:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='user_like',
            new_name='users_like',
        ),
    ]
