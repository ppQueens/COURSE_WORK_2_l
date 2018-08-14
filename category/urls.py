from django.urls import path
from . import views

app_name = "category"

urlpatterns = [
    path('new_test/<category>/', views.get_content, name='category'),
    path('new_test/', views.show_categories, name='show_cats'),
]
