from django.shortcuts import get_object_or_404, render_to_response

from core.models import Location
from mailit.views import get_list_or_post_CF

from .models import Video


def video_list(request):
    return get_list_or_post_CF(request, Video, 'videogallery/video_list.html',
                               {'section': 'video',
                               'locations': Location.objects.all()})


def video_detail(request, year, month, day, slug):
    import datetime
    import time
    date_stamp = time.strptime(year + month + day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    video = get_object_or_404(Video, pub_date__year=pub_date.year,
                              pub_date__month=pub_date.month,
                              pub_date__day=pub_date.day,
                              slug=slug)

    return render_to_response('videogallery/vdeo_detail.html',
                              {'video': video})
