from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html

from tinymce.models import HTMLField

from utils.aux_utils import get_image_path
from utils.storage import OverwriteStorage


class Slide(models.Model):

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    image = models.ImageField(
        upload_to=get_image_path, verbose_name=_("Image"),
        storage=OverwriteStorage(), blank=True, null=True)

    order = models.IntegerField(blank=True, verbose_name=_("Display order"))
    html = HTMLField(blank=True, null=True,
                     help_text=_("""You can use HTML markup - be careful!
                                  Don't copypaste from unknown sources"""),
                     verbose_name=_("Additional promo text")
                     )

    def image_tag(self):
        return format_html(
            u'<img src="{0}" style="max-height:100px;width:auto;"/>',
            self.image.url
        )
    def image_link(self):
      return self.image.url

    image_tag.short_description = _('Image')
    image_tag.allow_tags = True

    class Meta:
        verbose_name = _("Slide")
        verbose_name_plural = _("Slides")

    def __unicode__(self):
        return self.name

class Tab(models.Model):

    name = models.CharField(max_length=255, verbose_name=_("Tab name"))
    html = HTMLField(blank=True, null=True,
                     help_text=_("""You can use HTML markup - be careful!
                                  Don't copypaste from unknown sources"""),
                     verbose_name=_("Tab content")
                     )
    class Meta:
        verbose_name = _("Tab")
        verbose_name_plural = _("Tabs")

    def __unicode__(self):
        return self.name