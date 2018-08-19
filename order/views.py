from django.shortcuts import render
from cart.cart import Cart
from .models import OrderItem, Order
from .forms import OrderCreateForm
from django.db import transaction
from customer.models import Customer
# Create your views here.

@transaction.atomic()
def make_order(request):
    if request.POST:
        cart = Cart(request)

        print(request.POST)
        rp = request.POST
        form = OrderCreateForm(rp)

        if form.is_valid():
            print("IS_VALID_+++")
            order = Order.objects.create(customer=Customer.objects.get(customer__email=rp.get("email")),
                                         delivery_service=rp.get("delivery_service"),
                                         delivery_address=rp.get("delivery_address"),
                                         payment_method=rp.get("payment_method")
                                         )
            for item in cart:
                OrderItem.objects.create(order=order, item=item['item'], quantity=item['quantity'])
            cart.clear()
            return render(request,'created.html')
        else:
            print("IS NOT VALID")
            print(form.errors)
        # else:
        #     return HttpResponseRedirect("/new_test")
        # for item in cart:
        #     print(item['item'].itemimage_set.get())
            return render(request, 'checkout_form.html',
                          {'cart': cart, 'form': form})
    return render(request,"404.html")


