from django.conf.urls import patterns, url
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from photogallery.models import Photo
from django.views.generic.dates import DateDetailView

photo_view_params = {'queryset': Photo.objects.all(), 'date_field': "pub_date"}


urlpatterns = patterns('',
    

    url(r'^/?$', 'photogallery.views.render_albums',
       name='photogallery_list'),
    
    # url(r'^/?$', TemplateView.as_view(template_name="photogallery/photo_list.html")),
    
    
    url(r'^/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/?$', 
            DateDetailView.as_view(**photo_view_params),
            name='photogallery_photo_detail'),
    
    
   
)