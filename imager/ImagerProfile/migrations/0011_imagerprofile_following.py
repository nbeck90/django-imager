# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerprofile', '0010_auto_20150304_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerprofile',
            name='following',
            field=models.ManyToManyField(to='imagerprofile.ImagerProfile'),
            preserve_default=True,
        ),
    ]
