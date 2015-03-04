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
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='images', blank=True)),
                ('phone_number', models.CharField(max_length=20, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('phone_privacy', models.BooleanField(default=False)),
                ('birthday_privacy', models.BooleanField(default=False)),
                ('picture_privacy', models.BooleanField(default=False)),
                ('name_privacy', models.BooleanField(default=False)),
                ('email_privacy', models.BooleanField(default=False)),
                ('following', models.ManyToManyField(to='imagerprofile.ImagerProfile', null=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
