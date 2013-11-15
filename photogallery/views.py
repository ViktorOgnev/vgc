from django.shortcuts import render_to_response
from django.template import RequestContext

from core.models import Location

from .models import Album, Photo


class ObjectList():

    def __init__(self, title, list):
        self.title = title
        self.object_list = list


def render_albums(request):

    albums = Album.objects.all()
    result = []

    for album in albums:
        album_obj = ObjectList(album.title, [])
        for photo in Photo.objects.filter(albums=album.pk):
            album_obj.object_list.append(photo)

        result.append(album_obj)

    return render_to_response('photogallery/photo_list.html',
                              {'object_list': result,
                               'locations': Location.objects.all(),
                               'section': 'photo'},
                               context_instance=RequestContext(request))
