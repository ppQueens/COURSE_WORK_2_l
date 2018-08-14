from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from item.models import Item
from .cart import Cart
from .forms import CartAddItemForm
from django.core.serializers import serialize
from order.models import DeliveryService
from django.http import HttpResponse


@require_POST
def cart_add_item(request, item_slug):
    cart = Cart(request)
    print(request.POST)
    item = get_object_or_404(Item, slug=item_slug)
    form = CartAddItemForm(request.POST)
    if form.is_valid():
        print("cart adding form is valid")
        cd = form.cleaned_data
        cart.add(item=item, quantity=cd["quantity"], update_quantity=cd['update'])


    return redirect("cart:show_cart")

#TODO: индекс по slug
@require_POST
def cart_remove_item(request, item_slug):
    print(request.POST)
    cart = Cart(request)
    item = get_object_or_404(Item, slug=item_slug)
    cart.remove(item)
    return HttpResponse(cart.get_total_price())
        # redirect("cart:show_cart")


def show_cart(request):
    cart = Cart(request)
    return render(request, "cart_content.html", {"cart": cart})



def check_out_line(request):
    cart = Cart(request)
    delivery = DeliveryService.objects.all()
    return render(request, 'сheckout.html',
                  {'cart': cart, "delivery": delivery})
