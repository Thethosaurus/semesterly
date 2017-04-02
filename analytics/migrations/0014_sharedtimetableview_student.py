# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-08 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_merge'),
        ('analytics', '0013_sharedcourseview'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedtimetableview',
            name='student',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]