# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-31 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200730_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_html',
            field=models.TextField(blank=True, editable=False, verbose_name='正文HTML代码'),
        ),
    ]