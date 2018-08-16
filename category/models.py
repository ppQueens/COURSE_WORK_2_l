from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from st_app.models import CommonFields
from django.urls import reverse
from transliterate import translit
from django.db.models.signals import post_save
from django.db import transaction
import os



def get_image_path(instance,filename):
    return os.path.join('category/static/photos', "_".join(filename.split()))


class Category(MPTTModel, CommonFields):
    class Meta:
        db_table = "Category"
        verbose_name_plural = "Category"

    url_field = models.CharField(max_length=100, blank=False, default=None)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    cat_create_date = models.DateTimeField(auto_now_add=True, null=True)
    cat_update_date = models.DateTimeField(auto_now=True)
    main_page_filters = models.CharField(max_length=100, blank=True, default=None)
    cats_image = models.ImageField(upload_to=get_image_path, blank=True, default=None)


    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category:show_cats', args=[self.url_field])

@transaction.atomic()
def static_url(sender, instance, **kwargs):
    print(kwargs)
    # if kwargs["created"]:
    print(str(instance.cats_image))
    instance.cats_image = str(instance.cats_image).split("/", 2)[2]
    post_save.disconnect(static_url,sender=Category)
    instance.save(force_update=True)

post_save.connect(static_url, sender=Category)
