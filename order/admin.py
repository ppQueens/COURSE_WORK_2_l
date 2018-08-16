from django.contrib import admin
from .models import OrderItem, Order
# Register your models here.



class OrderItemAdmin(admin.StackedInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model = Order

    list_display = [field.name for field in Order._meta.fields]
    readonly_fields = ["total_price","order_code"]
    inlines = [OrderItemAdmin]


admin.site.register(Order, OrderAdmin)