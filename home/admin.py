from django.contrib import admin
from .models import Contact


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'subject', 'created_on')
    
    list_filter = ('subject', 'created_on')


admin.site.register(Contact, ContactAdmin)