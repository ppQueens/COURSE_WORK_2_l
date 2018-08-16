import hashlib
import time
import uuid

from django.core.validators import MinValueValidator
from django.db import models
from django.db import transaction
from django.db.models.signals import post_save
from django.urls import reverse

from category.models import Category
from customer.models import Customer
from st_app.models import Brand, CommonFields
from translates_word import categories


def _createHash():
    hash = hashlib.sha1()
    hash.update(str(time.time()).encode("ascii"))
    return hash.hexdigest()[:10]

class ItemFieldTypeValue(models.Model):
    field_type_id = models.AutoField(primary_key=True, unique=True)
    # field_type = models.CharField(max_length=100, null=True, blank=True, default=None)
    field_value = models.CharField(max_length=100, unique=True)
    unique_str_id = models.CharField(max_length=10, editable=False)

    def __str__(self):
        return "{0}".format(self.field_value)

    def __repr__(self):
        return "{0}".format(self.field_value)

    def save(self, *args, **kwargs):
        super(ItemFieldTypeValue, self).save(*args, **kwargs)


class ItemFieldTitle(models.Model):
    field_title_value_id = models.AutoField(primary_key=True, unique=True)
    field_title = models.CharField(max_length=100, unique=True)
    use_for = models.CharField(max_length=50, default=None, blank=True)

    def __str__(self):
        return "{0}".format(self.field_title)


class ItemField(models.Model):
    field_id = models.AutoField(primary_key=True, unique=True)
    # type = models.ForeignKey(ItemFieldTypeValue, max_length=100, null=True, blank=True)
    value = models.ForeignKey(ItemFieldTypeValue, max_length=100, default=None, on_delete=models.CASCADE)
    title = models.ForeignKey(ItemFieldTitle, max_length=100, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}-{1}".format(self.title, self.value)

    class Meta:
        unique_together = ['value', 'title']
        db_table = "ItemField"
        verbose_name_plural = "ItemField"


class Item(CommonFields):
    class Meta:
        db_table = "Item"
        verbose_name_plural = "Item"

    item_price = models.DecimalField(max_digits=10, decimal_places=3, default=0,
                                     validators=[MinValueValidator(0, "Price must be positive number!")])
    item_quantity = models.PositiveIntegerField(default=0,
                                                validators=[MinValueValidator(0, "Quantity must be positive number!")])

    item_short_desc = models.CharField(max_length=200, default=None, blank=True)
    item_category = models.ForeignKey(Category, default=None, blank=True, null=True, on_delete=models.CASCADE)
    item_create_date = models.DateTimeField(auto_now_add=True, null=True)
    item_update_date = models.DateTimeField(auto_now=True)
    item_published = models.BooleanField(default=False)
    item_metadata = models.CharField(max_length=500, default=None, blank=True)
    item_brand = models.ForeignKey(Brand, default=None, blank=True, null=True, on_delete=models.CASCADE)
    item_fields = models.ManyToManyField(ItemField, through='ItemFieldItem')
    slug = models.SlugField(max_length=60, default=None)
    main_image = models.CharField(max_length=500,blank=True, default=None)




    def get_absolute_url(self):

        return reverse('item:item_main', args=[categories[str(self.item_category).lower()], self.slug])

    def __str__(self):
        return self.title


import os


def get_image_path(instance, filename):
    part_number = ItemField.objects.filter(title__field_title="part_number",item__id=instance.item.id)\
        .values_list("value__field_value")[0]
    return os.path.join('item/static/photos', "_".join(instance.item.title.split()) +"_"+part_number[0], filename)

class ItemImage(models.Model):
    image_id = models.AutoField(primary_key=True, unique=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_path, blank=True, default=None)
    image_type = models.PositiveIntegerField(default=0)
    as_main = models.BooleanField(default=False)



    class Meta:
        db_table = "ItemImage"
        verbose_name_plural = "ItemImage"
        # instance.image = models.ImageField(upload_to=str(instance.image).split("/", 2)[2],blank=True,default=None)

@transaction.atomic()
def static_url(sender, instance, **kwargs):

    if kwargs["created"]:
        instance.image = str(instance.image).split("/", 2)[2]
        instance.save(force_update=True)
    if instance.as_main:
        instance.item.main_image = instance.image
        instance.item.save(force_update=True)


post_save.connect(static_url, sender=ItemImage)



class ItemFieldItem(models.Model):
    class Meta:
        db_table = "ItemFieldItem"
        unique_together = (("item", "item_field"),)

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_field = models.ForeignKey(ItemField, on_delete=models.CASCADE)
    use_as_customer_filter = models.BooleanField(default=False)
    use_as_common_detail = models.BooleanField(default=False)

    def __str__(self):
        return "{0}".format(self.item_field)

        # default = uuid.uuid4().hex[:6].lower( default=uuid.uuid4().hex[:6].lower())


def set_unique(sender, instance, **kwargs):
    if kwargs["created"]:
        instance.unique_str_id = uuid.uuid4().hex[:6].lower()
        instance.save(force_update=True)


post_save.connect(set_unique, sender=ItemFieldTypeValue)

# class ItemComment(CommonFields):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     date_time = models.DateTimeField(auto_now_add=True)
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
#     rating = models.SmallIntegerField(default=0)

