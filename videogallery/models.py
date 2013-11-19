import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from markdown2 import markdown

from core.models import Location
from vgc.settings import YOUTUBE_IMAGE_URL

class Video(models.Model):
    
    
    title = models.CharField(max_length=250,help_text='Maximum 250 characters.')
    link = models.CharField(max_length=250,help_text='Maximum 250 characters.')
    description = models.TextField()
    excerpt = models.TextField(blank=True, 
                            help_text='A short summary of the entry. Optional.')
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    
    excerpt_html = models.TextField(editable=False, blank=True)
    description_html = models.TextField(editable=False, blank=True)
    
    slug = models.SlugField(unique=True, help_text=""" Suggested value 
                        automatically generated from title. Must be unique.""")
                        
    
    thumb_url = models.CharField(max_length=250, editable=False, blank=True)
    embed_url = models.CharField(max_length=250, editable=False, blank=True)
    
    # featuring location
    locations = models.ManyToManyField(Location)
    
    def __unicode__(self):
        return self.title
    
    
    class Meta:
        
        verbose_name_plural = _("Videos")
        verbose_name = _("Video")
        ordering = ['-pub_date']
        
    def save(self, force_insert=False, force_update=False):
        splitted_url = self.link.split("/")
        youtube_video_id = splitted_url[-1]
        self.thumb_url = YOUTUBE_IMAGE_URL + youtube_video_id + "/hqdefault.jpg"
        
        
        self.embed_url = "http://www.youtube.com/embed/" + youtube_video_id
        self.description_html = markdown(self.description)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
            
        super(Video, self).save(force_insert, force_update)
    
    @models.permalink
    def get_absolute_url(self):
        return ('videogallery_video_detail', (),
               {'year': self.pub_date.strftime("%Y"),
                'month': self.pub_date.strftime("%b").lower(),
                'day' : self.pub_date.strftime("%d"),
                'slug': self.slug })
        