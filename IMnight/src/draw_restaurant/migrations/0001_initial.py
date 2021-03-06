# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-14 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_user', '0003_auto_20180114_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField(blank=True, default=0.8, null=True)),
                ('drawtime', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='my_user.Profile')),
            ],
        ),
    ]
