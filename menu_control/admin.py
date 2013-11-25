from django.contrib import admin

from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    fields = ('title', 'short_descr', 'section', 'side', 'content')

admin.site.register(MenuItem, MenuItemAdmin)