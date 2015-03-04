# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerprofile', '0007_imagerprofile_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagerprofile',
            name='following',
        ),
    ]
