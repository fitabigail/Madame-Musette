from django.contrib import admin
from .models import Contact, Designer
from django.utils.html import format_html


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'subject', 'created_on')
    
    list_filter = ('subject', 'created_on')


admin.site.register(Contact, ContactAdmin)


class DesignerAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 50px" />'.format(obj.image.url))

    list_display = ('id', 'image_tag', 'first_name', 'last_name', 'hierarchy',)

    list_display_links = ('image_tag', 'first_name')
    list_filter = ('hierarchy',)   


admin.site.register(Designer, DesignerAdmin)
