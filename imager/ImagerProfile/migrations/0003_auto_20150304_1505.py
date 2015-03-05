# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerprofile', '0002_auto_20150304_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='phone_number',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
