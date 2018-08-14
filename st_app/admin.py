

from order.models import *


from django.contrib import admin


def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


make_active.short_description = "Mark active"


def make_not(modeladmin, request, queryset):
    queryset.update(is_active=False)


make_not.short_description = "Mark not active"


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]
    actions = [make_active, make_not]


admin.site.register(Status, StatusAdmin)


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined',
                    'last_login']


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)





class OrderItemAdmin(admin.StackedInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model = Order

    list_display = [field.name for field in Order._meta.fields]
    readonly_fields = ["total_price"]

    inlines = [OrderItemAdmin]


admin.site.register(Order, OrderAdmin)





class DetailsManufacturer(admin.ModelAdmin):
    list_display = ('title', 'brand_web_site')


# admin.site.register(Brand, DetailsManufacturer)


