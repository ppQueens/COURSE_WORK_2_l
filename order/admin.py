from django.contrib import admin
from .models import DeliveryService
# Register your models here.



class DeliverySeriviceAdmin(admin.ModelAdmin):
    list_display = ("title","to_door","to_pickUp_point")

admin.site.register(DeliveryService,DeliverySeriviceAdmin)
