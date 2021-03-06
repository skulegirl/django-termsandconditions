# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-19 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('termsandconditions', '0004_termsandconditions_groups'), ('termsandconditions', '0005_auto_20180719_1545'), ('termsandconditions', '0006_auto_20180719_1546'), ('termsandconditions', '0007_auto_20180719_1548')]

    dependencies = [
        ('termsandconditions', '0003_auto_20170627_1217'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='termsandconditions',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='Leave empty to apply to all users, or add groups that these conditions apply to.', to='auth.Group'),
        ),
    ]
