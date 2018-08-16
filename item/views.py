from django.shortcuts import render

import translates_word

from .models import Item, ItemFieldItem, ItemField


# def show_item_processor(request):
#     q = Q()
#     if request.GET:
#         q = Q(item_fields__value__field_value=request.GET.get("series"))
#
#     processors = Item.objects.filter(item_category__title="процессоры").filter(q)
#
#     return render(request, 'processor.html', {"p": processors}, locals())
#


def item(request, category, item_slug):
    title = translates_word.reversed_categories[category]
    self_item = Item.objects.filter(item_category__title=title).get(slug=item_slug)
    title_detail = ItemField.objects.filter(item__id=self_item.id,title__use_for="title").values_list("value__field_value")
    #
    # for image in self_item.itemimage_set.all():
    #     print(type(str(image.image)))
    title_detail = " / ".join(i[0] for i in title_detail)
    # values_list(
    #     "item_field__value__field_value", "item_field__value__field_type")

    common_details = ItemFieldItem.objects.filter(item__slug=item_slug, use_as_common_detail=True).values_list(
        "item_field__title__field_title", "item_field__value__field_value")

    # warranty = self_item.item_fields.get(title__field_title="warranty")
    if request.method == "POST":
        return render(request, "item_content.html", locals())
    return render(request, 'item_main_template.html', locals())


def details(request):
    print(request.POST)
    full_details = ItemFieldItem.objects.filter(item__slug=request.POST.get("item_slug")).values_list(
        "item_field__title__field_title",
        "item_field__value__field_value")

    words = translates_word.values
    print(full_details)
    return render(request, "item_full_details.html", locals())


#
# @login_required(login_url="/signup/")
# def add_comment(request):
#     if request.POST:
#         form = NewCommentValid(request.POST)
#         if form.is_valid():
#             Comment.objects.create(about=Item.objects.get(id=int(form.data.get("item"))),
#                                    author=User.objects.get(email=form.data.get("email")), text=form.data.get("comment"))
#         else:
#             print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
#     return HttpResponseRedirect(request.path.rsplit("/", 2)[0])
#
#





def show_items(request, category):
    Item.objects.filter()
    pass


def show_filters(request, category):
    any_item = Item.objects.filter(item_category=category).first()
