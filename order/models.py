from django.db import models
from item.models import Item
from customer.models import Customer
from status.models import Status
from django.db.models.signals import post_save
from st_app.models import CommonFields
from django.contrib.auth.models import User


# class Payment(CommonFields):
#     #payment_id = models.AutoField(primary_key=True, unique=True)
#     payment_param = models.TextField()
#     #payment_description = models.TextField()
#     payment_datetime = models.DateTimeField(auto_now_add=True)
#     payment_currency = models.TextField(default=None)
#     payment_status = models.ForeignKey(Status, default=None)
#
#     class Meta:
#         db_table = "Payment"
#         verbose_name_plural = "Payment"


class DeliveryService(models.Model):
    title = models.CharField(max_length=70)
    to_door = models.BooleanField(default=False)
    to_pickUp_point = models.BooleanField(default=False)
    to_anywhere_else = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Order(models.Model):
    class Meta:
        unique_together = (('order_id', 'customer'),)
        ordering = ('-update_date',)

    DELIVERY_SERVICES = (
        (0,"DELIVERY_SERVICE_1"),
        (1,"DELIVERY_SERVICE_2"),
        (2,"DELIVERY_SERVICE_3")
    )

    order_id = models.AutoField(unique=True, primary_key=True)
    customer = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, default=None, null=True, blank=True,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True)
    delivery_service = models.ForeignKey(DeliveryService, default=None, null=True, blank=True,on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=100, default=None, null=True, blank=True)
    payment_method = models.CharField(max_length=100, default=None, null=True, blank=True)
    total_price = models.PositiveIntegerField(default=0)
    #items_in_order = models.ManyToManyField(Item, through='OrderItem')

    def __str__(self):
        return str(self.order_id)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

    # def get_total_cost(self):
    #     return sum(item.get_cost() for item in self.categories.all())


class OrderItem(models.Model):
    class Meta:
        db_table = "OrderItem"
        unique_together = (('item', 'order'),)

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

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
