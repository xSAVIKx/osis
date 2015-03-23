# coding=utf-8
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from easy_thumbnails.fields import ThumbnailerImageField
from web_site.util.upload_util import UploadTo, UploadToItemImage


class ThumbnailAdminMixin(object):
    admin_thumbnail_field = 'admin_thumbnail_field_name'

    def admin_thumbnail(self):
        admin_thumbnail_field = getattr(self, getattr(self, self.admin_thumbnail_field))
        if admin_thumbnail_field:
            thumbnail = admin_thumbnail_field['thumbnail']
            if thumbnail:
                return u'<a href="%s" target="_blank"><img src="%s" style="width: 250px;"/></a>' % (
                    admin_thumbnail_field.url, admin_thumbnail_field['thumbnail'].url)
            else:
                return u'<a href="%s" target="_blank"><img src="%s" style="width: 250px;"/></a>' % (
                    admin_thumbnail_field.url, admin_thumbnail_field.url)
        else:
            return u'(none)'

    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True


class Type(models.Model):
    title = models.CharField(max_length=50)
    parent_type = models.ForeignKey('Type', related_name='parent type', null=True, blank=True)


class Characteristic(models.Model):
    title = models.CharField(max_length=50)


class StringCharacteristicValue(models.Model):
    value = models.CharField(max_length=200)
    characteristic = generic.GenericRelation('Characteristic')


class IntegerCharacteristicValue(models.Model):
    value = models.IntegerField()
    characteristic = generic.GenericRelation('Characteristic')


class BooleanCharacteristicValue(models.Model):
    value = models.BooleanField(default=False)
    characteristic = generic.GenericRelation('Characteristic')


class Item(models.Model, ThumbnailAdminMixin):
    upload_dir = 'item_images'
    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    description = models.TextField(max_length=400, blank=True)
    description_short = models.TextField(max_length=50, default='')
    type = models.ForeignKey('Type', blank=True, null=True)
    logo_image = ThumbnailerImageField(upload_to=UploadTo(upload_dir))
    admin_thumbnail_field_name = 'logo_image'

    def __unicode__(self):
        return u"{0}".format(self.title)

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'item_id': str(self.id)})


class ItemImage(models.Model, ThumbnailAdminMixin):
    item = models.ForeignKey('Item', related_name='ItemImages')
    title = models.CharField(max_length=40, blank=True)
    image_file = ThumbnailerImageField(upload_to=UploadToItemImage(sub_path='images/'))
    admin_thumbnail_field_name = 'image_file'

    def __unicode__(self):
        return u"{0}_{1}".format(self.item.title, self.image_file.name)