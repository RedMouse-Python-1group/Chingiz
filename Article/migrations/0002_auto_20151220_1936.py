# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 19:36
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comments_text',
            field=tinymce.models.HTMLField(),
        ),
    ]
