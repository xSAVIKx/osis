# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from web_site.views import GalleryView, ItemListView, ItemDetailedView, AboutUsTemplateView, ContactUsView


__author__ = 'Iurii Sergiichuk'

urlpatterns = patterns('',

                       url(r'^gallery/$', GalleryView.as_view(), name='gallery'),
                       url(r'^contact_us/$', ContactUsView.as_view(), name='contact_us'),
                       url(r'^about_us/$', AboutUsTemplateView.as_view(), name='about_us'),
                       url(r'^catalog/$', ItemListView.as_view(), name='item_list'),
                       url(r'^catalog/(?P<item_id>\d+)/$', ItemDetailedView.as_view(), name="item_detail"),
                       url(r'', RedirectView.as_view(pattern_name='item_list'), name='index'),
)