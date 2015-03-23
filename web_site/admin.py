# coding=utf-8
from django.contrib import admin

# Register your models here.
from web_site.models import Item, ItemImage, Type, Characteristic, StringCharacteristicValue, \
    BooleanCharacteristicValue, \
    IntegerCharacteristicValue


class ItemImageInline(admin.TabularInline):
    model = ItemImage


class StringCharacteristicValueInline(admin.TabularInline):
    model = StringCharacteristicValue


class BooleanCharacteristicValueInline(admin.TabularInline):
    model = BooleanCharacteristicValue


class IntegerCharacteristicValueInline(admin.TabularInline):
    model = IntegerCharacteristicValue


class CharacteristicAdmin(admin.ModelAdmin):
    fields = ['title']
    list_display = ['title']


class ItemAdmin(admin.ModelAdmin):
    fields = ['title', 'description_short', 'description', 'price', 'type', 'logo_image']
    list_display = ('title', 'description_short', 'admin_thumbnail', )
    inlines = [ItemImageInline]


class ItemImageAdmin(admin.ModelAdmin):
    fields = ['title', 'item', 'image_file']
    list_display = ['item', 'image_file', 'admin_thumbnail', ]


admin.site.register(Type)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage, ItemImageAdmin)