from django.conf.urls import url
from . import views

app_name = "order"
urlpatterns = [
    url(r'^create/$', views.make_order, name='make_order'),

]