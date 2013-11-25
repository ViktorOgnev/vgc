from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Slide, Tab

def home_page(request):
    
    slides = Slide.objects.all().order_by("order")
    tabs = Tab.objects.all()

    context = {'slides': slides,
               'tabs': tabs}
    return render_to_response("core/home_page.html", context,
                              context_instance=RequestContext(request))
