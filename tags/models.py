from django.db import models
from item.models import Item


# Create your models here.




class Tag(models.Model):
    class Meta:
        db_table = "tags"
    id = models.AutoField(primary_key=True, unique=True)
    tag_name = models.CharField(max_length=100, default=None, blank=True)
    main = models.BooleanField(default=False)
    def __str__(self):
        return self.tag_name



class TagsCloud(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["tag", "item"]
