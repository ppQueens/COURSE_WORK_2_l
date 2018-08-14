from django.urls import path, re_path
from . import views

app_name = "customer"
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    # path('login/', views.login_view, name='login_view'),
    re_path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

]
