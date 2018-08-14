from django.urls import path
from . import views
from ajax_select import urls as ajax_select_urls


app_name = "cart"

urlpatterns = [
    path('show/', views.show_cart, name='show_cart'),
    path('add/<slug:item_slug>/', views.cart_add_item, name='cart_add_item'),
    path('remove/<slug:item_slug>/', views.cart_remove_item, name='cart_remove_item'),
    path('check_out/', views.check_out_line, name='cart_checking')
]
