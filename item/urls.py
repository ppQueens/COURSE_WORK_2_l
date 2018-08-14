from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path('new_test/<category>/<slug:item_slug>/', views.item, name='item_main'),
    path(r'details/', views.details, name='details'),
]
