from django.contrib import admin
from .models import Order, OrderProduct


# Register your models here.


class OrderProductAdminInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('orderitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderProductAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'address_line_1',
              'address_line_2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

