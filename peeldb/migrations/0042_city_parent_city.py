# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-05 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peeldb', '0041_assessmentdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='parent_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='peeldb.City'),
        ),
    ]
