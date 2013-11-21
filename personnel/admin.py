from django.contrib import admin
from .models import Employee, Specialisation


class EmployeeAdmin(admin.ModelAdmin):

    fields = ('name', 'slug', 'position', 'image', 'image_tag', 'bio', 'specialisation')
    filter_horizontal = ['specialisation']
    prepopulated_fields = {'slug': ['name']}
    field_options = {'classes': ['collapse', 'extrapretty'], }
    list_display = ['pk', 'image_tag', 'name', 'image', ]
    list_display_links = ('pk', 'image_tag', 'name',)
    search_fields = ['name', 'specialisation__name', ]
    list_filter = ['name', 'specialisation__name', ]
    readonly_fields = ('image_tag',)
    ordering = ['name']
    save_as = True

admin.site.register(Employee, EmployeeAdmin)


class SpecialisationAdmin(admin.ModelAdmin):

    fields = ('name', 'slug',  'image', 'image_tag',)
    prepopulated_fields = {'slug': ['name']}
    field_options = {'classes': ['collapse', 'extrapretty'], }
    list_display = ['pk', 'image_tag', 'name', 'image', ]
    list_display_links = ('pk', 'image_tag', 'name',)
    search_fields = ['name']
    list_filter = ['name']
    readonly_fields = ('image_tag',)
    ordering = ['name']
    save_as = True

admin.site.register(Specialisation, SpecialisationAdmin)
