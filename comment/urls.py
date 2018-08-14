from django.urls import path
from . import views
from ajax_select import urls as ajax_select_urls

app_name = "comment"

urlpatterns = [
    path('comments/show/<slug:item_slug>', views.get_comments, name='show_comments'),
    path('comments/add/<slug:item_slug>', views.add_comment, name='add_comment'),
]
