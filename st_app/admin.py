

from order.models import *


from django.contrib import admin


def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


make_active.short_description = "Mark active"


def make_not(modeladmin, request, queryset):
    queryset.update(is_active=False)


make_not.short_description = "Mark not active"


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined',
                    'last_login']


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)











class DetailsManufacturer(admin.ModelAdmin):
    list_display = ('title', 'brand_web_site')


# admin.site.register(Brand, DetailsManufacturer)


