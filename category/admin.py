from django.contrib import admin
from .models import Category
from item.models import Item, ItemFieldItem
# Register your models here.

from mptt.admin import MPTTModelAdmin



#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Category.objects.filter()]
#
class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ['title', 'parent']

    change_form_template = "admin-checkboxes.html"

    def change_view(self, request, object_id, form_url='', extra_context=None):

        response = super().change_view(
            request,
            object_id,
            form_url=form_url,
            extra_context=extra_context,
        )
        if not request.POST:
            #field_title    используется для именования фильтров
            #use_as_customer_filter используется пометки фильтра как используемого
            #field_title_value_id   используется для связывания label и checkbox
            customer_filters = Item.objects.filter(item_category__id=object_id).values_list(
                "item_fields__title__field_title","itemfielditem__use_as_customer_filter",
                "item_fields__title__field_title_value_id").distinct()
            response.context_data["my_data"] = customer_filters
            print(customer_filters)

        else:
            check_customer_filters = ItemFieldItem.objects.filter(item__item_category=object_id,
                                    item_field__title__field_title__in=request.POST._getlist("customer_filters"))
            ItemFieldItem.objects.filter(item__item_category=object_id).update(use_as_customer_filter=False)
            check_customer_filters.update(use_as_customer_filter=True)

        return response




admin.site.register(Category, CustomMPTTModelAdmin)
