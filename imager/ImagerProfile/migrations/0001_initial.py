# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_picture', models.ImageField(upload_to=b'')),
                ('phone_number', models.CharField(max_length=15)),
                ('birthday', models.DateField()),
                ('picture_privacy', models.BooleanField()),
                ('phone_privacy', models.BooleanField()),
                ('birthday_privacy', models.BooleanField()),
                ('name_privacy', models.BooleanField()),
                ('email_privacy', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
