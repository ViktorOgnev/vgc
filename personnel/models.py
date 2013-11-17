from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.utils.html import format_html

from utils.aux_utils import get_image_path
from utils.storage import OverwriteStorage


class PersonnelBase(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    slug = models.SlugField(max_length=255)

    image = models.ImageField(
        upload_to=get_image_path, verbose_name=_("Image"),
        storage=OverwriteStorage(), blank=True, null=True)
    
    def image_tag(self):
    	return format_html(
    		u'<img src="{0}" style="max-height:100px;width:auto;"/>',
			self.image.url
		)
	
	image_tag.short_description = _('Image')
	image_tag.allow_tags = True

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def save(self, force_insert=False, force_update=False):
        if not self.slug:
            self.slug = slugify(self.name)
        super(PersonnelBase, self).save(force_insert, force_update)


class Specialisation(PersonnelBase):

    description = models.CharField(
        max_length=255, verbose_name=_("Description"))
    

    class Meta:
        verbose_name = _("Specialisation")
        verbose_name_plural = _("Specialisation")


class Employee(PersonnelBase):

    bio = models.TextField(blank=True, verbose_name=_("Biography"))
    specialisation = models.ManyToManyField(Specialisation)

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")

# post_delete.connect(cache_evict, sender=Employee)
# post_save.connect(cache_update, sender=Employee)
# post_save.connect(create_thumbnail, sender=Employee)
