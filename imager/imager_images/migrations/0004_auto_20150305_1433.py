# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0003_auto_20150305_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerphoto',
            name='title',
            field=models.CharField(default=b'MyPhoto', max_length=20),
            preserve_default=True,
        ),
    ]
