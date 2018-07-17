# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-14 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_id', models.CharField(max_length=11)),
                ('clientid', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('registration', models.CharField(default='', max_length=50)),
                ('expiry', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
