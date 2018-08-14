from django.shortcuts import render
from cart.cart import Cart
from .models import OrderItem, DeliveryService, Order
from .forms import OrderCreateForm
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
# Create your views here.

@transaction.atomic()
def make_order(request):


    if request.POST:
        delivery = DeliveryService.objects.all()
        cart = Cart(request)

        print(request.POST)
        rp = request.POST
        form = OrderCreateForm(rp)

        if form.is_valid():
            print("IS_VALID")
            order = Order.objects.create(customer=User.objects.get(email__iexact=rp.get("email")),
                                         delivery_service=delivery.get(id=rp.get("delivery_service")),
                                         delivery_address=rp.get("delivery_address"),
                                         payment_method=rp.get("payment_method")
                                         )
            #order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        item=item['item'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request,
                          'created.html',
                          {'order': order})
        else:
            print("IS NOT VALID")
        # else:
        #     return HttpResponseRedirect("/new_test")
        # for item in cart:
        #     print(item['item'].itemimage_set.get())
            return render(request, 'сheckout.html',
                          {'cart': cart, 'form': form, "delivery":delivery})
    return render(request,"404.html")


