# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-27 03:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VoteApp', '0011_uservoterecord_isdelete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uComName',
        ),
    ]
