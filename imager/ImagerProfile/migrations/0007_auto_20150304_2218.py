# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerprofile', '0006_auto_20150304_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='following',
            field=models.ManyToManyField(related_name='followers', null=True, to='imagerprofile.ImagerProfile'),
            preserve_default=True,
        ),
    ]
