from django.db import models

# from mptt.models import MPTTModel

# from category.models import Category
# from item.models import Item


# Create your models here.



class CommonFields(models.Model):
    class Meta:
        abstract = True

    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, default=None)
    description = models.TextField(default=None, blank=True)


class Brand(CommonFields):
    class Meta:
        db_table = "brand"

    brand_web_site = models.CharField(default=None, blank=True, max_length=70)

    def __str__(self):
        return self.title

#
