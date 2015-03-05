# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0002_auto_20150305_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerphoto',
            name='picture',
            field=models.ImageField(upload_to=b'images'),
            preserve_default=True,
        ),
    ]
