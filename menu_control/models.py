from django.db import models
from django.utils.translation import ugettext_lazy as _


from core.models import Entry


class MenuItem(models.Model):

    LEFT = 1
    RIGHT = 2
    ABOUT = 3
    ARTICLES = 4

    SIDE_CHOICES = (
        (LEFT, _('Left Side')),
        (RIGHT, _('Right Side')),
    )

    SECTION_CHOICES = (
        (ABOUT, _('About Section')),
        (ARTICLES, _('Articles section')),
    )

    REDIRECT_CHOICES = ()

    title = models.CharField(max_length=255)
    short_descr = models.TextField(blank=True, null=True)
    section = models.IntegerField(
        choices=SECTION_CHOICES, verbose_name=_("Section of menu"))

    side = models.IntegerField(choices=SIDE_CHOICES, default=LEFT)

    content = models.ForeignKey(Entry,
                                verbose_name=_("Content"),
                                limit_choices_to={'internal_status__exact': 2})

    class Meta:
        verbose_name = _('Menu item')
        verbose_name_plural = _('Menu items')

    def __unicode__(self):
        return self.title
