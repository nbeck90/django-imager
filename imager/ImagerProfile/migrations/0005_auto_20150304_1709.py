# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerprofile', '0004_auto_20150304_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='following',
            field=models.ManyToManyField(related_name='+', null=True, to='imagerprofile.ImagerProfile'),
            preserve_default=True,
        ),
    ]
