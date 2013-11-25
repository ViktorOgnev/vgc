from django.conf.urls import patterns, include, url
from filebrowser.sites import site

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^/?$', 'homepage.views.home_page', name='homepage'),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    #url(r'^accounts/register/?$', 'accounts.views.register', name="register"),
    url(r'^photogallery/', include('photogallery.urls')),
    url(r'^videogallery', include('videogallery.urls')),
    url(r'^personnel/', include('personnel.urls')),
    url(r'', include('core.urls')),
    )
