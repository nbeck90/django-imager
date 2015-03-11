# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageralbum',
            name='published',
            field=models.CharField(default=b'public', max_length=7, choices=[(b'public', b'Public'), (b'private', b'Private'), (b'shared', b'Shared')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imageralbum',
            name='title',
            field=models.CharField(default=b'MyAlbum', max_length=63),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerphoto',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerphoto',
            name='published',
            field=models.CharField(default=b'public', max_length=31, choices=[(b'public', b'Public'), (b'private', b'Private'), (b'shared', b'Shared')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerphoto',
            name='title',
            field=models.CharField(default=b'MyPhoto', max_length=31),
            preserve_default=True,
        ),
    ]
