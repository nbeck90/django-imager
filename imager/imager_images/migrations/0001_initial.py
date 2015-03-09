# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerAlbum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'MyAlbum', max_length=50)),
                ('description', models.TextField(blank=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_published', models.DateField(null=True, blank=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('published', models.CharField(default=b'public', max_length=20, choices=[(b'public', b'Public'), (b'private', b'Private'), (b'shared', b'Shared')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImagerPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'MyPhoto', max_length=20)),
                ('picture', models.ImageField(upload_to=b'images')),
                ('description', models.CharField(max_length=20, blank=True)),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('date_published', models.DateField(null=True, blank=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('published', models.CharField(default=b'public', max_length=20, choices=[(b'public', b'Public'), (b'private', b'Private'), (b'shared', b'Shared')])),
                ('albums', models.ManyToManyField(related_name='photos', null=True, to='imager_images.ImagerAlbum', blank=True)),
                ('user', models.ForeignKey(related_name='photos', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='imageralbum',
            name='cover',
            field=models.ForeignKey(related_name='+', blank=True, to='imager_images.ImagerPhoto', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imageralbum',
            name='user',
            field=models.ForeignKey(related_name='albums', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
