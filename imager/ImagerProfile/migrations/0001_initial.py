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
                ('profile_picture', models.ImageField(upload_to=b'')),
                ('phone_number', models.CharField(max_length=15)),
                ('birthday', models.DateField()),
                ('picture_privacy', models.BooleanField(default=False)),
                ('phone_privacy', models.BooleanField(default=False)),
                ('birthday_privacy', models.BooleanField(default=False)),
                ('name_privacy', models.BooleanField(default=False)),
                ('email_privacy', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
