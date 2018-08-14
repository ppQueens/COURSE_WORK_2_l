from django.shortcuts import render
from .models import Category
from django.db.models import Q,F, Func, Value
from item.models import Item, ItemField, ItemFieldItem, ItemFieldTitle, ItemFieldTypeValue
from decimal import Decimal
from .translates_word import fields
from django.db.models import Count, Sum
from .translates_word import reversed_categories, categories
from django.urls import reverse
from django.db.models.functions import Concat
# Create your views here.



def freq(category):
    d = {}
    frequency = Item.objects.filter(item_category__title=category,
                                    item_fields__title__field_title="frequency").values_list(
        "item_fields__title__field_title")
    # ItemField.objects.values_list("value__field_value").filter(title__field_title="frequency")
    all_freq = tuple(map(lambda x: float(*x), list(frequency)))
    d["max"], d["avr"], d["min"] = round(max(all_freq), 1), round(sum(all_freq) / len(all_freq), 1), round(
        min(all_freq), 1)
    return d

# helpfull_functions = {"frequency":freq}


def show_categories(request):
    hardware_cats = Category.objects.extra(
        where=["rght - lft = 1 and parent_id is not null and (parent_id = 15 or mptt_level = 2)"]).order_by("id")
    network_hardware_cats = Category.objects.extra(where=["parent_id = 17"]).order_by("id")
    peripheral_hardware_cats = Category.objects.extra(where=["parent_id = 23"]).order_by("id")

    links_for = ("processors","motherboards") #add some on demand
    links_for_cat = dict(hardware_cats.filter(url_field__in=links_for).values_list("url_field","url_field"))

    return render(request, "starter-page-listing.html", locals())




def set_filters(request, category):
    q = Q()
    free = True
    items = Item.objects.filter(item_category=category)
        # annotate(abs_url=F("slug")). \

    # , itemimage__as_main = True
        # values("title", "item_price", "item_quantity", "itemimage__image", "slug", "abs_url", "item_category")

    if request.POST.get("free") == "":
        free = False
    if request.POST and free:
        print(request.POST)
        for i in request.POST:
            if i != "min" and i != "max" and i != "orderby":
                some_list = request.POST.getlist(i)
                items = items.filter(item_fields__value__unique_str_id__in=some_list).distinct()

        if request.POST.get("min"):
            items = items.filter(item_price__gte=Decimal(request.POST.get("min")))
        if request.POST.get("max"):
            items = items.filter(item_price__lte=Decimal(request.POST.get("max")))
        q = Q(id__in=items.values_list("id").filter())


    return q, items


def get_items(request, category):
    q, items = set_filters(request, Category.objects.filter(url_field=category).get())
    price = items.values_list("item_price", flat=True)

    max_price = round(max(price), 0)
    min_price = round(min(price), 0)

    if request.POST.get("orderby") == "cheapest":
        q_sort = "item_price"
    elif request.POST.get("orderby") == "priciest":
        q_sort = "-item_price"
    else:
        q_sort = "id"
    items = items.filter(q).order_by(q_sort)

    return locals()



def get_content(request, category):
    print(category)
    items = get_items(request,category)


    title = reversed_categories[category]
    # if not request.POST:
    aside = get_filters(category)

    # else:
    #     return render(request, "items.html", locals())
    return render(request, "some_category_page.html", locals())



def get_filters(category):
    customer_filters = ItemFieldItem.objects.filter(item__item_category__url_field=category,
                                                    use_as_customer_filter=True).values_list(
        "item_field__title__field_title",
        "item_field__value__field_value",
        "item_field__value__unique_str_id").distinct()
    dict_key_value = dict()
    dict_secret_human = dict()
    for i in customer_filters:
        key = i[0]
        if not dict_key_value.get(key):
            dict_key_value[key] = [i[2]]
        else:
            dict_key_value[key].append(i[2])
        dict_secret_human[i[2]] = i[1]
    translate = fields

    return locals()



