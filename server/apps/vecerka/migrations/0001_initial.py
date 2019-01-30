# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-27 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=12, max_digits=20)),
                ('latitude', models.DecimalField(decimal_places=12, max_digits=20)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.CharField(max_length=300, verbose_name='description')),
            ],
        ),
    ]
