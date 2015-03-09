# coding=utf-8
from django.utils.deconstruct import deconstructible

__author__ = 'Iurii Sergiichuk'


@deconstructible
class UploadTo(object):
    upload_dir = u"{0}/{1}/{2}{3}"

    def __init__(self, initial_folder='', sub_path=''):
        self.initial_folder = initial_folder
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        return self.upload_dir.format(self.initial_folder, instance.title, self.sub_path, filename)


class UploadToItemImage(UploadTo):
    def __call__(self, instance, filename):
        return self.upload_dir.format(instance.item.upload_dir, instance.item.title,
                                      self.sub_path, filename)