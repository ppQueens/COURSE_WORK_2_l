from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from st_app.models import CommonFields
from django.urls import reverse
from transliterate import translit
from django.db.models.signals import post_save


class Category(MPTTModel, CommonFields):
    class Meta:
        db_table = "Category"
        verbose_name_plural = "Category"


    url_field = models.CharField(max_length=100,blank=False, default=None)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',on_delete=models.CASCADE)
    cat_create_date = models.DateTimeField(auto_now_add=True, null=True)
    cat_update_date = models.DateTimeField(auto_now=True)
   # filters = models.BooleanField(default=None)

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category:show_cats', args=[self.url_field])


#
# def toggle_filter_state(sender, instance, **kwargs):
#     order = instance.order
#
#     #filter = instance.Category.objeect
#     all_order_items = OrderItem.objects.filter(order=order)
#
#     total_price = 0
#     for orderItem in all_order_items:
#         total_price += orderItem.item.item_price * orderItem.quantity
#
#     order.total_price = total_price
#     order.save(force_update=True)
#
# #pre_save.co
# post_save.connect(toggle_filter_state, sender=Category)
