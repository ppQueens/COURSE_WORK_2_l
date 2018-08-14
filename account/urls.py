from django.urls import path, re_path
from . import views

app_name = "account"


urlpatterns = [
    path("login/",views.user_login, name="login"),
    path("logout/",views.user_logout, name="logout"),
    path("register/",views.user_register, name="register"),
    re_path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),

]