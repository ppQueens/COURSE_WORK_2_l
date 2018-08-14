from django.db import models
from django.contrib.auth.models import User
from item.models import Item

# Create your models here.


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, unique=True)
    item = models.ForeignKey(Item,on_delete=models.CASCADE, related_name="comments",null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, null=True)
    phone_email = models.CharField(max_length=30, null=True)
    # author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    text = models.TextField(max_length=1000, blank=False,null=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "Comment"
        ordering = ("created",)




# class UserComments(models.Model):
#     user = models.ForeignKey(User)
#     comment = models.ForeignKey(Comment)