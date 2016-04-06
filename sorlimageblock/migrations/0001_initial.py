# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', sorl.thumbnail.fields.ImageWithThumbnailsField(upload_to=b'images/%Y/%m/%d')),
                ('caption', models.TextField(blank=True)),
                ('alt', models.CharField(max_length=100, null=True, blank=True)),
                ('lightbox', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImagePullQuoteBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', sorl.thumbnail.fields.ImageWithThumbnailsField(upload_to=b'images/%Y/%m/%d')),
                ('caption', models.TextField(blank=True)),
                ('alt', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
