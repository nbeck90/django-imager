# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerprofile', '0003_auto_20150303_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='images'),
            preserve_default=True,
        ),
    ]
