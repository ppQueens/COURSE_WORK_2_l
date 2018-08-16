from django.db import models
from item.models import Item
from customer.models import Customer
from django.db.models.signals import post_save
from st_app.models import CommonFields
from django.contrib.auth.models import User
import hashlib, time




class Order(models.Model):
    status_choice = (
        ("new", "NEW"),
        ("processed", "PROCESSED"),
        ("sent", "SENT"),
        ("canceled", "CENCELED"),
        ("need clarification", "NEED CLARIFICATION"),
        ("fulfilled", "FULFILLED")
    )

    class Meta:
        db_table = "Order"
        unique_together = (('order_id', 'customer'),)
        ordering = ('-update_date',)



    order_id = models.AutoField(unique=True, primary_key=True)
    customer = models.ForeignKey(Customer, default=None, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=14, choices=status_choice, default=status_choice[0])
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True)
    delivery_service = models.CharField(max_length=100, default=None, null=True, blank=True)
    delivery_address = models.CharField(max_length=100, default=None, null=True, blank=True)
    payment_method = models.CharField(max_length=100, default=None, null=True, blank=True)
    total_price = models.PositiveIntegerField(default=0)
    order_code = models.CharField(max_length=10, default=0, blank=True, editable=False)


    def __str__(self):
        return str(self.order_id)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)



class OrderItem(models.Model):
    class Meta:
        db_table = "OrderItem"
        unique_together = (('item', 'order'),)

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=1)
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "order: {}".format(self.order.order_id)

    def save(self, *args, **kwargs):
        super(OrderItem, self).save(*args, **kwargs)


def calc_total_price(sender, instance, **kwargs):
    order = instance.order
    all_order_items = OrderItem.objects.filter(order=order)

    total_price = 0
    for orderItem in all_order_items:
        total_price += orderItem.item.item_price * orderItem.quantity

    order.total_price = total_price
    order.save(force_update=True)


post_save.connect(calc_total_price, sender=OrderItem)


def _createHash():
    hash = hashlib.sha1()
    hash.update(str(time.time()).encode("ascii"))
    return hash.hexdigest()[:10]


def set_unique(sender, instance, **kwargs):
    if kwargs["created"]:
        instance.order_code = _createHash().upper()
        instance.save(force_update=True)


post_save.connect(set_unique, sender=Order)
