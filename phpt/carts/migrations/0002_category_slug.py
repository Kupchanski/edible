# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-15 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='categ'),
        ),
    ]