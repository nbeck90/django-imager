# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageralbum',
            name='cover',
            field=models.ForeignKey(related_name='+', blank=True, to='imager_images.ImagerPhoto', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imageralbum',
            name='published',
            field=models.CharField(default=b'public', max_length=20, choices=[(b'public', b'Public'), (b'private', b'Private'), (b'shared', b'Shared')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagerphoto',
            name='albums',
            field=models.ManyToManyField(related_name='photos', to='imager_images.ImagerAlbum'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imageralbum',
            name='date_created',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imageralbum',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imageralbum',
            name='title',
            field=models.CharField(default=b'MyAlbum', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imageralbum',
            name='user',
            field=models.ForeignKey(related_name='photos', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerphoto',
            name='published',
            field=models.CharField(default=b'public', max_length=20, choices=[(b'public', b'Public'), (b'private', b'Private'), (b'shared', b'Shared')]),
            preserve_default=True,
        ),
    ]
