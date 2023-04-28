from django.contrib import admin
from .models import Product, Category
from django.utils.html import format_html



class ProductAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 50px" />'.format(obj.image.url))

    list_display = ('image_tag', 'sku', 'name', 'category', 'price', 'rating',)
    list_display_links = ('image_tag', 'sku', 'name',)
    search_fields = ('sku', 'name', 'category', 'rating',)
    list_filter = ('category', 'rating',)

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

