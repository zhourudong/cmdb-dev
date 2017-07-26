# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-16 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('op', '0006_auto_20161116_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='superviser',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_superviser', to='account.User', verbose_name='\u5ba1\u6279\u4eba'),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_projowner', to='account.User', verbose_name='\u7533\u8bf7\u4eba'),
        ),
    ]