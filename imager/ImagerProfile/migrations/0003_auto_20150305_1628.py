# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerprofile', '0002_auto_20150305_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='blocking',
            field=models.ManyToManyField(related_name='+', null=True, to='imagerprofile.ImagerProfile', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='following',
            field=models.ManyToManyField(related_name='followers', null=True, to='imagerprofile.ImagerProfile', blank=True),
            preserve_default=True,
        ),
    ]
