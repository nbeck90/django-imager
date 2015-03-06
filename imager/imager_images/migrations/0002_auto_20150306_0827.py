# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageralbum',
            name='user',
            field=models.ForeignKey(related_name='albums', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerphoto',
            name='user',
            field=models.ForeignKey(related_name='photos', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
