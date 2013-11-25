from django.contrib import admin

from .models import Slide, Tab


class SlideAdmin(admin.ModelAdmin):

    fields = ('order', 'name', 'image', 'image_tag', 'text')
    field_options = {'classes': ['collapse', 'extrapretty'], }
    list_display = ['pk','image_tag', 'image']
    list_display_links = ('pk', 'image_tag',)
    readonly_fields = ('image_tag',)
    save_as = True

admin.site.register(Slide, SlideAdmin)


class TabAdmin(admin.ModelAdmin):

    fields = ('name', 'html',)
    field_options = {'classes': ['collapse', 'extrapretty'], }
    list_display = ['pk', 'name']
    list_display_links = ('pk', 'name',)
    search_fields = ['name']
    list_filter = ['name']
    save_as = True

admin.site.register(Tab, TabAdmin)
