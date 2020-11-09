from django.urls import path
from carts.views import cart, cart_update, checkout_home
app_name = 'cart'
urlpatterns = [
    path('', cart , name='cart'),
    path('update/', cart_update , name='update'),
    path('checkout/', checkout_home , name='checkout'),
]
