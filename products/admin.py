from django.contrib import admin
from .models import Product, Category, Customise
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" height="50" \
             style="border-radius: 50px" />'.format(obj.image.url))

    list_display = ('id', 'image_tag', 'name', 'category', 'price',
                    'in_stock', 'is_customised', 'updated_date')
    list_display_links = ('image_tag', 'name')
    list_filter = ('category', 'rating', 'is_customised', 'updated_date')
    list_per_page = 20
    list_editable = ('in_stock', 'is_customised',)

    ordering = ('id',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CustomisedAdmin(admin.ModelAdmin):
    list_display = ('product', 'sole', 'color',
                    'special_size', 'created_date')
    list_filter = ('product', 'sole',
                   'color', 'special_size')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customise, CustomisedAdmin)
