# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerprofile', '0009_relationship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='relationship_from',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='relationship_to',
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
    ]
