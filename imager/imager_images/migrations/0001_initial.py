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
                ('title', models.CharField(default=b'MyAlbum', max_length=20)),
                ('description', models.CharField(max_length=20, blank=True)),
                ('date_created', models.DateField(null=True, blank=True)),
                ('date_published', models.DateField(null=True, blank=True)),
                ('date_modified', models.DateField(null=True, blank=True)),
                ('user', models.OneToOneField(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImagerPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'MyAlbum', max_length=20)),
                ('picture', models.ImageField(null=True, upload_to=b'images', blank=True)),
                ('description', models.CharField(max_length=20, blank=True)),
                ('date_uploaded', models.DateField(null=True, blank=True)),
                ('date_published', models.DateField(null=True, blank=True)),
                ('date_modified', models.DateField(null=True, blank=True)),
                ('published', models.CharField(default=b'Public', max_length=20, choices=[(b'Pubic', b'Public'), (b'Private', b'Private'), (b'Shared', b'Shared')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
