# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerprofile', '0008_remove_imagerprofile_following'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField()),
                ('relationship_from', models.ForeignKey(related_name='+', to='imagerprofile.ImagerProfile')),
                ('relationship_to', models.ForeignKey(related_name='+', to='imagerprofile.ImagerProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
