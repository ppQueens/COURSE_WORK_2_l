from django.contrib import admin
from .models import *
from django.utils.text import slugify

# Register your models here.



class ItemFieldAdmin(admin.StackedInline):
    model = ItemFieldItem
    extra = 1


class ItemFieldTitleAdmin(admin.StackedInline):
    model = ItemFieldTitle
    extra = 1


class ItemFieldTypeValueAdmin(admin.StackedInline):
    model = ItemFieldTypeValue
    extra = 1


class ItemImageAdmin(admin.StackedInline):
    model = ItemImage
    extra = 1

# from tags.models import Tag,TagsCloud
#
# class TagsCloudAdmin(admin.StackedInline):
#     model = TagsCloud
#     extra = 3
#
#
# admin.site.register(Tag)





class ItemAdmin(admin.ModelAdmin):
    class Meta:
        model = Item

    list_display = ('title', 'item_price', 'item_category', 'item_quantity', 'item_create_date', 'item_published',)
    inlines = [ItemFieldAdmin, ItemImageAdmin] #TagsCloudAdmin
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Item, ItemAdmin)


admin.site.register(ItemFieldTypeValue, admin.ModelAdmin)


admin.site.register(ItemField, admin.ModelAdmin)

admin.site.register(ItemFieldTitle, admin.ModelAdmin)
