# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

from web_site import urls as web_site_url
from web_site.views import ContactUsView
from osis import settings


urlpatterns = patterns('',
                       url(r'^admin_tools/', include('admin_tools.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^send_email$', ContactUsView.as_view(), name='send_email'),
                       url(r'', include(web_site_url)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
