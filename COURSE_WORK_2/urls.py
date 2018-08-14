from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('st_app.urls')),
                  path('', include('category.urls', namespace="category")),
                  path('', include('item.urls', namespace="item")),
                  path('', include('customer.urls', namespace="customer")),
                  # path('logout/', logout, {'next_page': "/new_test/"}, name='logout'),
                  path('cart/', include("cart.urls", namespace="cart")),
                  path('orders/', include('order.urls', namespace='order')),
                  path('account/', include('account.urls',namespace="account")),
                    path("",include("comment.urls",namespace="comment"))
              ] + static("st_app/static/photos/ItemImage_object/")
