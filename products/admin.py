from django.contrib import admin
from .models import Product, Category
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 50px" />'.format(obj.image.url))

    list_display = ('id', 'image_tag', 'name', 'category', 'price', 'is_available',
                    'updated_date')
    list_display_links = ('image_tag', 'name',)
    search_fields = ('name', 'category', 'rating', 'is_available', 'updated_date')
    list_filter = ('category', 'rating', 'is_available', 'updated_date')

    ordering = ('id',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)