from django.contrib import admin
from .models import Comment
# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('phone_email','name', 'item', 'created', 'active')
    list_filter = ('active', 'created', 'modified')
    search_fields = ('phone_email','name' 'text')