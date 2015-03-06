# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0004_auto_20150305_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageralbum',
            name='date_modified',
            field=models.DateField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerphoto',
            name='date_modified',
            field=models.DateField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerphoto',
            name='date_uploaded',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
