# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydjapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-title',)},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=models.TextField(editable=b'False'),
        ),
    ]