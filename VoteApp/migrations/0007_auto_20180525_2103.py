# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-25 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VoteApp', '0006_auto_20180525_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'ordering': ['-cVotes']},
        ),
    ]
