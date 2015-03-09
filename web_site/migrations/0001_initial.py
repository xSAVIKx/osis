# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields

import web_site.util.upload_util
import web_site.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('price', models.PositiveIntegerField(default=0, blank=True)),
                ('description', models.TextField(max_length=200, blank=True)),
                ('logo_image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=web_site.util.upload_util.UploadTo(b'item_images'))),
            ],
            options={
            },
            bases=(models.Model, web_site.models.ThumbnailAdminMixin),
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, blank=True)),
                ('image_file', easy_thumbnails.fields.ThumbnailerImageField(upload_to=web_site.util.upload_util.UploadToItemImage(sub_path=b'images/'))),
                ('item', models.ForeignKey(related_name='ItemImages', to='web_site.Item')),
            ],
            options={
            },
            bases=(models.Model, web_site.models.ThumbnailAdminMixin),
        ),
    ]
