# coding=utf-8
from django.contrib import admin

# Register your models here.
from web_site.models import Item, ItemImage


class ItemAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'logo_image']
    list_display = ('title', 'logo_image', 'admin_thumbnail', )


class ItemImageAdmin(admin.ModelAdmin):
    fields = ['title', 'item', 'image_file']
    list_display = ['item', 'image_file', 'admin_thumbnail', ]


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage, ItemImageAdmin)