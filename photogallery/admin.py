from django.contrib import admin
from photogallery.models import Photo, Album


class PhotoAdmin(admin.ModelAdmin):

    fields = ('title', 'slug', 'image_file', 'image_tag', 'excerpt', 'description', 'link',
              'albums', 'locations' )
    filter_horizontal = ['albums', 'locations']
    prepopulated_fields = {'slug': ['title'], 'description':['excerpt']}
    field_options = {'classes': ['collapse', 'extrapretty'], }
    list_display = ['title', 'image_tag', 'pk', 'slug', 'pub_date']
    search_fields = ['pk', 'title', 'pub_date', 'albums__title']
    list_filter = ['pub_date', 'albums__title']
    date_hierarchy = 'pub_date'
    ordering = ['-pub_date']
    readonly_fields = ('image_tag',)
    save_as = True


class AlbumAdmin(admin.ModelAdmin):

    list_filter = ['pub_date']
    prepopulated_fields = {'slug': ['title']}
    date_hierarchy = 'pub_date'


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
