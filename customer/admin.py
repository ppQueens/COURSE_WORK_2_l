from django.contrib import admin
from .models import Customer
from .models import *
# Register your models here.


# class InlineUser(admin.StackedInline):
#     model = User
#
# class UserProfileAdmin(admin.ModelAdmin):
#
#     inlines = [InlineUser]
#
admin.site.register(Customer)